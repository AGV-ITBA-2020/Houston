import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from parse import *
import matplotlib.pyplot as plt
from MapManager import MapManager
from NetworkManager import NetworkManager


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setWindowTitle('ITBAGV v0') ##Nombre de la app y su ícono
        self.setWindowIcon(QtGui.QIcon("AGV Icon.png"))
        self.setCentralWidget(self._main)
        layout = QtWidgets.QGridLayout(self._main) #Organización de la GUI (grilla de widgets)

        self.log = QtWidgets.QTextEdit() #Log de msgs
        self.log.setReadOnly(True)
        layout.addWidget(self.log, 0, 0)

        self.figure = plt.figure()      #Figura donde se plotea el mapa
        self.canvas = FigureCanvas(self.figure)
        self.map = MapManager()
        self.canvas.draw_idle()

        layout.addWidget(self.canvas,0,1)
        self.addToolBar(NavigationToolbar(self.canvas, self))

        self.command = QtWidgets.QLineEdit()
        self.command.editingFinished.connect(self.enter_press)

        self.flo = QtWidgets.QFormLayout()
        self.flo.addRow("Comandos", self.command)
        layout.addWidget(self.command,1,0,1,2)

        self.command_mapping = {"M {:d} {:d}":self.start_mission,"SetPos {:d} {:d}":self.set_position} #Diccionario que condiciona los formatos de entrada de comandos

        self.nm=NetworkManager()
        self.nm.set_read_callback(self.parse_tcp_msg)
        self.nm.set_new_agv_callback(self.new_agv)
    def enter_press(self):
        self.last_command = self.command.text()
        valid_command=False;
        for key in self.command_mapping:
            if parse(key, self.last_command): #Si cumple el formato de alguno de los comandos, ejecuta la función que implica cada uno
                self.command_mapping[key]()
                valid_command = True;
        if  valid_command == False:
            self.log.append("Invalid Command")
        self.command.clear()
    def set_position(self):
        res = parse("SetPos {:d} {:d}", self.last_command)
    def start_mission(self):
        res = search("M {:d} {:d}", self.last_command)
        self.mission = self.map.get_path(res[0], res[1])
        msg_to_send= "new mission \n" + self.mission
        if not self.nm.has_msgs_pending(1):
            self.nm.send(1,msg_to_send)
            self.log.append("New mission:" + self.mission)
        self.log.append("AGV 1 has a pending message to send")

    def new_agv(self,AGVn):
        self.map.update_agv_pos(AGVn, 1, 2)
        self.canvas.draw_idle()
    def parse_tcp_msg(self,AGVn, msg):
        self.log.append("AGV "+ str(AGVn) +": "+msg)
        #procesamiento

if __name__ == "__main__":
    # Check whether there is already a running QApplication (e.g., if running
    # from an IDE).
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)

    app = ApplicationWindow()
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec_()
