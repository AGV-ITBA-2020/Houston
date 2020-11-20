import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from parse import *
import matplotlib.pyplot as plt
from MapManager import MapManager
import paho.mqtt.client as mqtt
from AGV_status import AGV_status
import re

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
        self.nt=NavigationToolbar(self.canvas, self)
        self.addToolBar(self.nt)

        self.command = QtWidgets.QLineEdit()
        self.command.editingFinished.connect(self.enter_press)

        self.flo = QtWidgets.QFormLayout()
        self.flo.addRow("Comandos", self.command)
        layout.addWidget(self.command,1,0,1,2)

        #Comandos permitidos de entrada
        self.command_mapping ={re.compile('(SM) [0-9]*$',re.I): self.start_mission,  #Misión simple
                               re.compile('(setPos) [0-9]*$',re.I): self.set_position,  # Misión simple
                               re.compile('[s] [0-9]*$',re.I): self.setVel,
                               re.compile('(LM) ([HBDN] [0-9]* )*[HBDN]$', re.I): self.start_long_mission, #Misión larga: LM para indicar misión, luego serie de eventos y nodos a llegar y al final el evento final. B=button, D=delay, H=houston continue N=None
                               re.compile('[C]$', re.I): self.continueMission
                               }
        #MQTT Mosquitto config
        self.mqttClient = mqtt.Client("Houston")  # create new instance
        self.mqttClient.on_message = self.parse_msg
        self.mqttClient.connect("localhost")  # connect to broker
        self.mqttClient.subscribe("Houston")
        self.mqttClient.loop_start()

        self.agv_status_dict = {};#Status de los AGVs que se conecten
        self.log.textChanged.connect(self.clearMsgBlock)

        #self.agv_status_dict[1] = AGV_status(1) #Para debuggear
        #self.map.update_agv_pos(1, 1, 1, 0)
    ############ Callbacks #####################
    def enter_press(self):      #Enter luego de poner un comando en el text input.
        self.last_command = self.command.text()
        valid_command=False;
        for key in self.command_mapping: #Me fijo todos los formatos que especifiqué de antemano
            #if parse(key, self.last_command): #formato con parse
            if key.match(self.last_command):
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
        aux=self.log.toPlainText()
        if len(aux)>500:
            self.log.clear()
            self.log.append(aux[250:])
    #### Funciones útiles
    def gen_mission_block(self, steps, dists): ##Dados los steps y las distancias, genera el texto que lo representa para enviar por mqtt
        mission = "Bs" #Block start
        for i in range(int(len(steps)/2)):
            mission += dists[i] + steps[(i*2):(i*2+2)]; #Pone por ejemplo 11Fr14Sl1
        mission += "Be" #Block end
        return mission
    def IBECharToString(self, char):
        dict= {'B':"Button",'H':"Houston",'D':"Delay",'N':"None"}
        return dict[char.upper()]
    def IBECharToMQTTFormat(self, char):
        dict= {'B':"Bu",'H':"Ho",'D':"De",'N':"No"}
        return dict[char.upper()]
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
        res = search("SM {:d}", self.last_command)
        steps_str,node_path,dist_list = self.map.get_path(self.agv_status_dict[1].in_node, res[0])
        msg_to_send= "Quest?\n" + "No"+self.gen_mission_block(steps_str, dist_list)+"No"
        self.agv_status_dict[1].new_mission([node_path],[dist_list], ["None", "None"]) #Las IBE son none por ser una misión simple
        self.mqttClient.publish("AGV1", msg_to_send)
        self.log.append("New mission:" + steps_str)
    def start_long_mission(self):
        IBE = re.findall("[HBND]", self.last_command)                   ##Letras que indican IBE
        node_obj=list(map(int,re.findall(" [0-9]* ",self.last_command))) ##Lista con todos los nodos finales de bloques en formato int
        prev_node=self.agv_status_dict[1].in_node ##Variables que voy a usar en el loop. Este nodo es donde parte el agv.
        node_path_list =[]; path_dists_list = [];
        msg_to_send = self.IBECharToMQTTFormat(IBE[0])
        for n_block in range(len(node_obj)): ##Para cada bloque
            steps_str, node_path, path_dists = self.map.get_path(prev_node, node_obj[n_block]) #Obtiene el camino más corto y guarda en las listas correspondientes
            node_path_list.append(node_path);path_dists_list.append(path_dists)
            msg_to_send += self.gen_mission_block(steps_str, path_dists)+self.IBECharToMQTTFormat(IBE[n_block+1]) #Pasa el camino del grafo al formato de internet, cierra el bloque y agrega el texto del IBE que va en el msg
            prev_node=node_obj[n_block]
        IBE_list = [self.IBECharToString(i) for i in IBE]               ##Se pasan letras que significan IBE a palabras para la lógica de misión
        self.agv_status_dict[1].new_mission(node_path_list, path_dists_list,IBE_list)  # Las IBE son none por ser una misión simple
        self.mqttClient.publish("AGV1", msg_to_send)
        self.log.append("New mission: " + msg_to_send)
    def continueMission(self):
        self.mqttClient.publish("AGV1", "Continue")
        self.agv_status_dict[1].continue_mission()

if __name__ == "__main__":
    # Crea todo lo de QT y corre la clase de arriba
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)

    app = ApplicationWindow()
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec_()
