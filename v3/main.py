
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Battery import Battery
from Backend import Backend
import sys
from ui_design import Ui_MainWindow
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.fig = plt.figure(figsize=(10, 10), dpi=50, facecolor=(1, 1, 1), edgecolor=(0, 0, 0))
        plt.axis('off')
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas, self)
        lay = QVBoxLayout(self)
        lay.addWidget(self.toolbar)
        lay.addWidget(self.canvas)

    def update_plot(self):
        self.canvas.draw()

class MainWindow(QMainWindow):#Si crashea cambiar el tiempo de refresco
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.setWindowIcon(QIcon("AGV.png"))
        self.ui.setupUi(self)
        self.add_map_plot()
        self.ui.battery = Battery();
        self.ui.layout_plot_battery.addWidget(self.ui.battery)
        self.backend = Backend(self.ui.log,self.ui.battery)
        self.gui_light_map = {0: self.ui.agv_data_flag_in_mission,
                              1: self.ui.agv_data_flag_mission_paused,
                              2: self.ui.agv_data_flag_waiting_for_IBE,
                              3: self.ui.agv_data_flag_emergency,
                              4: self.ui.agv_data_flag_error,
                              5: self.ui.agv_data_flag_waiting_for_continue
                              }
        self.setWindowTitle('ITBAGV')
        startSize = QSize(1280, 800)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        self.m.update_plot()
        self.set_button_callbacks()
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_buttons_page)
        self.ui.block_count=1;
        self.ui.max_blocks=11;
        self.create_lists();
        self.update_ui()
        self.show()
        ## ==> END ##
    def add_map_plot(self):
        #Agrego el canvas de matplotlib que no se puede poner desde qt
        self.m=MatplotlibWidget();
        self.ui.verlayout_plot_panel = QVBoxLayout(self.ui.plot_frame)
        self.ui.verlayout_plot_panel.addWidget(self.m)
        self.flags_poll_timer = QTimer()
        self.flags_poll_timer.timeout.connect(self.update_interface)
        self.flags_poll_timer.start(1000)  ##Si se crashea, al ponerle un timer más alto parece ser menos probable que crashee-> puede ser que matplotlib tarde mucho en plotear el grafo y si hay que plotear de vuelta no le gusta?
    def create_lists(self):
        self.ui.IBE_list=[self.ui.IBE_1,self.ui.IBE_2,self.ui.IBE_3,self.ui.IBE_4,self.ui.IBE_5,self.ui.IBE_6,
                          self.ui.IBE_7,self.ui.IBE_8,self.ui.IBE_9,self.ui.IBE_10,self.ui.IBE_11,self.ui.IBE_12]
        self.ui.dest_list=[self.ui.dest_1,self.ui.dest_2,self.ui.dest_3,self.ui.dest_4,self.ui.dest_5,self.ui.dest_6,
                           self.ui.dest_7,self.ui.dest_8,self.ui.dest_9,self.ui.dest_10,self.ui.dest_11]
    def enter_command(self):
        input=self.ui.command_entry.text();
        if input: #Para eliminar que se mande vacío de consola
            retVal=self.backend.parse_cmd(self.ui.command_entry.text())
            self.ui.command_entry.clear()
            if retVal: #Si no se reconocio ningun comando, se comunica.
                self.ui.log.append(retVal)
    def is_mission_valid(self):
        return False;
    def flag_by_index(self,index):
        retVal=False;
        if(index==0):
            retVal=self.backend.agv_status_dict[1].in_mission
        elif (index==1):
            retVal=self.backend.agv_status_dict[1].paused
        elif (index == 2):
            retVal = self.backend.agv_status_dict[1].waiting_for_IBE
        elif (index == 3):
            retVal = self.backend.agv_status_dict[1].emergency
        elif (index == 4):
            retVal = self.backend.error
        elif (index == 5):
            retVal = self.backend.agv_status_dict[1].is_waiting_for_houston_continue()
        return retVal;
    def update_interface(self):

        if self.backend.check_for_map_updates():
            self.backend.map.draw_system();
            self.m.update_plot()

        for key in self.gui_light_map:  # Me fijo todos los formatos que especifiqué de antemano
            if self.flag_by_index(key):
                self.gui_light_map[key].setPixmap(QPixmap("icons/green-led-on.png"))
            else:
                self.gui_light_map[key].setPixmap(QPixmap("icons/led-red-on.png"))
    def update_ui(self):
        if(self.ui.stackedWidget.currentWidget()==self.ui.mission_page):
            for i in range(self.ui.max_blocks):
                if i < self.ui.block_count:
                    self.ui.dest_list[i].setVisible(True)
                    self.ui.IBE_list[i+1].setVisible(True)
                else:
                    self.ui.dest_list[i].setVisible(False)
                    self.ui.IBE_list[i + 1].setVisible(False)
        elif (self.ui.stackedWidget.currentWidget() == self.ui.main_buttons_page):
            if(self.backend.error):
                self.ui.but_abort_mission.setEnabled(False)
                self.ui.but_new_mission.setEnable(False)
                self.ui.but_pause_or_continue(False)
            else:
                if not self.backend.agv_status_dict[1].in_mission:
                    self.ui.but_abort_mission.setEnabled(False)
                    self.ui.but_new_mission.setEnabled(True)
                    self.ui.but_pause_or_continue.setEnabled(False)
                else:
                    self.ui.but_new_mission.setEnable(False)
    def set_button_callbacks(self):
        self.ui.but_reset.clicked.connect(lambda : self.backend.parse_cmd("r"))
        self.ui.but_select_log.clicked.connect(lambda :self.page_changed("log_page"))
        self.ui.but_back_to_missions.clicked.connect(lambda :self.page_changed("main_buttons_page"))
        self.ui.but_cancel_new_mission.clicked.connect(lambda :self.page_changed("main_buttons_page"))
        self.ui.but_new_mission.clicked.connect(lambda :self.page_changed("mission_page"))
    def page_changed(self,new_page):
        if(new_page=="log_page"):
            self.ui.stackedWidget.setCurrentWidget(self.ui.log_page)
        elif(new_page=="main_buttons_page"):
            self.ui.stackedWidget.setCurrentWidget(self.ui.main_buttons_page)
        elif(new_page=="mission_page"):
            self.ui.stackedWidget.setCurrentWidget(self.ui.mission_page)
        self.update_ui();


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
