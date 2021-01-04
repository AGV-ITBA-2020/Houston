
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
        self.ui.command_entry.editingFinished.connect(self.enter_command)

        self.gui_light_map = {0: self.ui.agv_data_flag_in_mission,
                              1: self.ui.agv_data_flag_mission_paused,
                              2: self.ui.agv_data_flag_waiting_for_IBE,
                              3: self.ui.agv_data_flag_emergency,
                              4: self.ui.agv_data_flag_error,
                              5: self.ui.agv_data_flag_waiting_for_continue
                              }
        ## SET ==> WINDOW TITLE
        self.setWindowTitle('ITBAGV')
        startSize = QSize(1280, 800)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        self.m.update_plot()
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

    def enter_command(self):
        input=self.ui.command_entry.text();
        if input: #Para eliminar que se mande vacío de consola
            retVal=self.backend.parse_cmd(self.ui.command_entry.text())
            self.ui.command_entry.clear()
            if retVal: #Si no se reconocio ningun comando, se comunica.
                self.ui.log.append(retVal)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
