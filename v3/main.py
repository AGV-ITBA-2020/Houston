
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
        self.ui.pause_icon = QIcon()
        self.ui.pause_icon.addFile(u"icons/16x16/cil-media-pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.continue_icon = QIcon()
        self.ui.continue_icon.addFile(u"icons/16x16/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_map_plot()
        self.ui.battery = Battery();
        self.ui.layout_plot_battery.addWidget(self.ui.battery)
        self.backend = Backend(self.ui.log, self.ui.battery)

        self.configure_mission_blocks_page();
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


        self.update_ui_inputs()
        self.show()
        ## ==> END ##
    def add_map_plot(self):
        #Agrego el canvas de matplotlib que no se puede poner desde qt
        self.m=MatplotlibWidget();
        self.ui.verlayout_plot_panel = QVBoxLayout(self.ui.plot_frame)
        self.ui.verlayout_plot_panel.addWidget(self.m)
        self.flags_poll_timer = QTimer()
        self.flags_poll_timer.timeout.connect(self.periodic_update_interface)
        self.flags_poll_timer.start(1000)  ##Si se crashea, al ponerle un timer más alto parece ser menos probable que crashee-> puede ser que matplotlib tarde mucho en plotear el grafo y si hay que plotear de vuelta no le gusta?
    def configure_mission_blocks_page(self):
        self.ui.block_count = 1;
        self.ui.max_blocks = 11;
        self.ui.IBE_list=[self.ui.IBE_1,self.ui.IBE_2,self.ui.IBE_3,self.ui.IBE_4,self.ui.IBE_5,self.ui.IBE_6,
                          self.ui.IBE_7,self.ui.IBE_8,self.ui.IBE_9,self.ui.IBE_10,self.ui.IBE_11,self.ui.IBE_12]
        self.ui.dest_list=[self.ui.dest_1,self.ui.dest_2,self.ui.dest_3,self.ui.dest_4,self.ui.dest_5,self.ui.dest_6,
                           self.ui.dest_7,self.ui.dest_8,self.ui.dest_9,self.ui.dest_10,self.ui.dest_11]
        station_list=self.backend.map.get_station_nodes();
        station_list_str = [str(i) for i in station_list]
        for i in range(self.ui.max_blocks):
            self.ui.dest_list[i].addItems(station_list_str)
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
    def gen_mission_command(self):
        command="Lm "+ self.backend.IBEStringToChar(self.ui.IBE_1.currentText())
        for i in range(self.ui.block_count):
            command += " "  + self.ui.dest_list[i].currentText() + " " + self.backend.IBEStringToChar(self.ui.IBE_list[i+1].currentText())
        return command;
    def is_mission_valid(self): ##TBD
        cmd=self.gen_mission_command()
        return self.backend.is_mission_cmd_valid(cmd)
    def periodic_update_interface(self):
        if self.backend.check_for_map_updates():
            self.backend.map.draw_system();
            self.m.update_plot()
        for key in self.gui_light_map:  # Me fijo todos los formatos que especifiqué de antemano
            if self.flag_by_index(key):
                self.gui_light_map[key].setPixmap(QPixmap("icons/green-led-on.png"))
            else:
                self.gui_light_map[key].setPixmap(QPixmap("icons/led-red-on.png"))
        self.update_ui_inputs()
    def update_ui_inputs(self): ##Update de cosas que no son ni las imágenes de los leds ni el mapa.
        if(self.ui.stackedWidget.currentWidget()==self.ui.mission_page):
            for i in range(self.ui.max_blocks):
                if i < self.ui.block_count:
                    self.ui.dest_list[i].setVisible(True)
                    self.ui.IBE_list[i+1].setVisible(True)
                else:
                    self.ui.dest_list[i].setVisible(False)
                    self.ui.IBE_list[i + 1].setVisible(False)
            self.ui.but_send_mission.setEnabled(self.is_mission_valid());
        elif (self.ui.stackedWidget.currentWidget() == self.ui.main_buttons_page):
            if(self.backend.error):
                self.ui.but_abort_mission.setEnabled(False)
                self.ui.but_new_mission.setEnabled(False)
                self.ui.but_pause_or_continue.setEnabled(False)
            else:
                if not self.backend.agv_status_dict[1].in_mission: #Si no está en misión, puede enviar una nueva y no pueda abortarlas/pausarlas
                    self.ui.but_abort_mission.setEnabled(False)
                    self.ui.but_pause_or_continue.setEnabled(False)
                    self.ui.but_new_mission.setEnabled(not self.backend.agv_status_dict[1].mission_sent) #No se pone enabled hasta que se acepte la misión.
                else:
                    self.ui.but_new_mission.setEnabled(False)
                    self.ui.but_abort_mission.setEnabled(True)

                    if self.backend.agv_status_dict[1].emergency or self.backend.agv_status_dict[1].paused or self.backend.agv_status_dict[1].waiting_for_IBE: #Solo en estos estados se muestra continue en vez de pausa
                        self.ui.but_pause_or_continue.setText("Continue")
                        self.ui.but_pause_or_continue.setIcon(self.ui.continue_icon)
                        self.ui.but_pause_or_continue.setEnabled(self.backend.agv_status_dict[1].is_waiting_for_houston_continue()) #Continue solo habilitado cuando se puede esperar eso del agv
                    else:
                        self.ui.but_pause_or_continue.setText("Pause")
                        self.ui.but_pause_or_continue.setIcon(self.ui.pause_icon)
                        self.ui.but_pause_or_continue.setEnabled(True)  ##Solo deshabilitado cuando espera por IBE
    def set_button_callbacks(self):
        self.ui.but_reset.clicked.connect(lambda : self.backend.parse_cmd("R"))
        self.ui.but_abort_mission.clicked.connect(lambda: self.backend.parse_cmd("A"))
        self.ui.but_pause_or_continue.clicked.connect(lambda: self.backend.parse_cmd("P" if self.ui.but_pause_or_continue.text()=="Pause" else "C"))
        self.ui.but_select_log.clicked.connect(lambda :self.page_changed("log_page"))
        self.ui.but_back_to_missions.clicked.connect(lambda :self.page_changed("main_buttons_page"))
        self.ui.but_cancel_new_mission.clicked.connect(lambda :self.page_changed("main_buttons_page"))
        self.ui.but_new_mission.clicked.connect(lambda :self.page_changed("mission_page"))
        self.ui.but_new_mission_steps.clicked.connect(lambda :self.n_block_changed("Added"))
        self.ui.but_rmv_mission_block.clicked.connect(lambda :self.n_block_changed("Removed"))
        self.ui.but_send_mission.clicked.connect(self.send_new_mission)
        self.ui.IBE_list[0].currentIndexChanged.connect(self.update_ui_inputs)
        for i in range(self.ui.max_blocks): ##Cada vez que se elige algo de las checkboxes de misión, se actualiza para ver si la misión se puede hacer
            if i < self.ui.block_count:
                self.ui.dest_list[i].currentIndexChanged.connect(self.update_ui_inputs)
                self.ui.IBE_list[i + 1].currentIndexChanged.connect(self.update_ui_inputs)

    def n_block_changed(self,change):
        if(change=="Added" and self.ui.block_count < self.ui.max_blocks):
            self.ui.block_count += 1
        if (change == "Removed" and self.ui.block_count > 1):
            self.ui.block_count -= 1
        self.update_ui_inputs()
    def page_changed(self,new_page):
        if(new_page=="log_page"):
            self.ui.stackedWidget.setCurrentWidget(self.ui.log_page)
        elif(new_page=="main_buttons_page"):
            self.ui.stackedWidget.setCurrentWidget(self.ui.main_buttons_page)
        elif(new_page=="mission_page"):
            self.ui.stackedWidget.setCurrentWidget(self.ui.mission_page)
        self.update_ui_inputs();
    def send_new_mission(self): ##Solo se permite llamar a esta función cuando ya se validó que es una misión posible
        self.backend.parse_cmd(self.gen_mission_command())
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_buttons_page)
        self.update_ui_inputs()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
