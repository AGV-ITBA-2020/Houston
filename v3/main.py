
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

        self.fig = plt.figure(figsize=(7, 5), dpi=65, facecolor=(1, 1, 1), edgecolor=(0, 0, 0))

        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas, self)
        lay = QVBoxLayout(self)
        lay.addWidget(self.toolbar)
        lay.addWidget(self.canvas)

    def update_plot(self):
        self.canvas.draw()

class MainWindow(QMainWindow):#QMainWindow
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
        self.setup_data_analysis()


        ## SET ==> WINDOW TITLE
        self.setWindowTitle('ITBAGV')
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        self.show()
        ## ==> END ##
    def add_map_plot(self):
        #Agrego el canvas de matplotlib que no se puede poner desde qt
        self.m=MatplotlibWidget();
        self.ui.verlayout_plot_panel = QVBoxLayout(self.ui.plot_frame)
        self.ui.verlayout_plot_panel.addWidget(self.m)

    def setup_data_analysis(self):
        self.flags_poll_timer = QTimer()
        self.flags_poll_timer.timeout.connect(self.update_interface)
        self.flags_poll_timer.start(500)
    def enter_command(self):
        retVal=self.backend.parse_cmd(self.ui.command_entry.text())
        self.ui.command_entry.clear()
        if  retVal == False: #Si no se reconocio ningun comando, se comunica.
            self.ui.log.append("Invalid Command")
    def update_interface(self):

        if self.backend.check_for_map_updates():
             self.m.update_plot()
        if self.backend.agv_status_dict[1].in_mission:
            self.ui.agv_data_flag_in_mission.setPixmap(QPixmap("icons/green-led-on.png"))
        else:
            self.ui.agv_data_flag_in_mission.setPixmap(QPixmap("icons/led-red-on.png"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
