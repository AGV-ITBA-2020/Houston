import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from parse import *
import matplotlib.pyplot as plt
from MapManager import MapManager
import paho.mqtt.client as mqtt
from AGV_status import AGV_status

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self): #Crea todo lo de la GUI
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
        self.map = MapManager()     #Map manager
        self.canvas.draw_idle()

        layout.addWidget(self.canvas,0,1)
        self.addToolBar(NavigationToolbar(self.canvas, self))

        self.command = QtWidgets.QLineEdit()
        self.command.editingFinished.connect(self.enter_press)

        self.flo = QtWidgets.QFormLayout()
        self.flo.addRow("Comandos", self.command)
        layout.addWidget(self.command,1,0,1,2)

        #Comandos permitidos de entrada
        self.command_mapping = {"M {:d} {:d}":self.start_mission,"SetPos {:d}":self.set_position,"S {:d} {:d}":self.setVel, "K {:f} {:f} {:f}":self.setPIDKs} #Diccionario que condiciona los formatos de entrada de comandos

        #MQTT Mosquitto config
        self.mqttClient = mqtt.Client("Houston")  # create new instance
        self.mqttClient.on_message = self.parse_msg
        self.mqttClient.connect("localhost")  # connect to broker
        self.mqttClient.subscribe("Houston")
        self.mqttClient.loop_start()

        self.agv_status_dict = {};#Status de los AGVs que se conecten
        self.log.textChanged.connect(self.clearMsgBlock)
    ############ Callbacks #####################
    def enter_press(self):      #Enter luego de poner un comando en el text input.
        self.last_command = self.command.text()
        valid_command=False;
        for key in self.command_mapping: #Me fijo todos los formatos que especifiqué de antemano
            if parse(key, self.last_command): #Si cumple el formato de alguno de los comandos, ejecuta la función que implica cada uno
                self.command_mapping[key]()
                valid_command = True;
        if  valid_command == False: #Si no se reconoció ningun comando, se comunica.
            self.log.append("Invalid Command")
        self.command.clear()

    def parse_msg(self,client, userdata, message): ##Parseo de mensajes de MQTT
        msg=str(message.payload.decode("utf-8"))
        AGVn = int((msg.split('\n', 1)[0]).split('V',1)[1])
        msg = msg.split('\n', 1)[1]  # Me quedo con los datos del agv
        self.log.append("AGV " + str(AGVn) + ": " + msg)
        if msg == "Online":
            self.agv_status_dict[AGVn] = AGV_status(AGVn)
            prev, next, distance = self.agv_status_dict[AGVn].get_agv_pos_nodes()
            self.map.update_agv_pos(AGVn, prev, next, distance)
            self.canvas.draw_idle()
        elif msg=="Quest step reached":
            if self.agv_status_dict[AGVn].in_mission:
                self.agv_status_dict[AGVn].mission_step_reached()
                prev, next, distance =self.agv_status_dict[AGVn].get_agv_pos_nodes()
                self.map.update_agv_pos(AGVn, prev, next, distance)
                self.canvas.draw_idle()
            else:
                print("Error")
        elif "Status" in msg:
            self.agv_status_dict[AGVn].distanceTravelled = search("DistanceTravelled {:d}", msg)[0]
            prev, next, distance = self.agv_status_dict[AGVn].get_agv_pos_nodes()
            self.map.update_agv_pos(AGVn, prev, next, distance)
            self.canvas.draw_idle()

    def clearMsgBlock(self): ##Máximo número de caracteres en el log (esto era por si se iba de memoria)
        if len(self.log.toPlainText())>100:
            self.log.clear()
    #### Funciones llamadas por comandos ###
    def setPIDKs(self):
        res = parse("K {:f} {:f} {:f}", self.last_command)
        msg_to_send = "Set K PID\n" + str(res[0])+ " " + str(res[1])+ " " + str(res[2]);
        self.mqttClient.publish("AGV1",msg_to_send)
    def setVel(self):
        res = parse("S {:d} {:d}", self.last_command)
        msg_to_send = "Fixed speed\n" + str(res[0])+ " " + str(res[1]);
        self.mqttClient.publish("AGV1",msg_to_send)
    def set_position(self):
        res = parse("SetPos {:d}", self.last_command)
        self.agv_status_dict[1].set_pos(self, res[0])
    def start_mission(self):
        res = search("M {:d} {:d}", self.last_command)
        steps_str,node_path,dist_list = self.map.get_path(res[0], res[1])
        msg_to_send= "Quest?\n" + self.gen_mission_block(steps_str, dist_list)
        self.agv_status_dict[1].new_mission([node_path],[dist_list], ["None", "None"]) #Las IBE son none por ser una misión simple
        self.mqttClient.publish("AGV1", msg_to_send)
        self.log.append("New mission:" + steps_str)
    def gen_mission_block(self, steps, dists):
        mission = "Bs" #Block start
        for i in range(int(len(steps)/2)):
            mission += dists[i] + steps[(i*2):(i*2+2)]; #Pone por ejemplo 11Fr14Sl1
        mission += "Be" #Block end
        return mission

if __name__ == "__main__":
    # Crea todo lo de QT
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)

    app = ApplicationWindow()
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec_()
