from MapManager import MapManager
import re
import paho.mqtt.client as mqtt
from Battery import Battery
from AGV_status import AGV_status
from parse import *


class Backend:
    def __init__(self,log,canvas,battery):
        self.map = MapManager()
        self.log = log;
        self.canvas = canvas;
        self.battery = battery;
        # Estructura de comandos aceptados por consola
        self.command_mapping = {re.compile('(SM) [0-9]*$', re.I): self.start_mission,  # Misión simple
                                re.compile('(setPos) [0-9]*$', re.I): self.set_position,  # Misión simple
                                re.compile('[s] [0-9]*$', re.I): self.setVel,
                                re.compile('[B] [0-9]*$', re.I): self.setBat, #Pone nivel de batería
                                re.compile('(LM) ([HBDN] [0-9]* )*[HBDN]$', re.I): self.start_long_mission,
                                # Misión larga: LM para indicar misión, luego serie de eventos y nodos a llegar y al final el evento final. B=button, D=delay, H=houston continue N=None
                                re.compile('[C]$', re.I): self.continueMission
                                }
        self.mqttClient = mqtt.Client("Houston")  # create new instance
        self.mqttClient.on_message = self.parse_mqtt_msg
        self.mqttClient.connect("localhost")  # connect to broker
        self.mqttClient.subscribe("Houston")
        self.mqttClient.loop_start()
        self.agv_status_dict = {};  # Status de los AGVs que se conecten
        self.agv_status_dict[1] = AGV_status(1)  # Para debuggear ya lo dejamos creado al agv1
        self.map.update_agv_pos(1, 1, 1, 0)
    def parse_cmd(self,cmd):
        valid_command = False;
        self.last_command=cmd
        for key in self.command_mapping:  # Me fijo todos los formatos que especifiqué de antemano
            # if parse(key, self.last_command): #formato con parse
            if key.match(cmd):
                valid_command = self.command_mapping[key]()
        return valid_command
    def parse_mqtt_msg(self,client, userdata, message): ##Parseo de mensajes de MQTT
        msg=str(message.payload.decode("utf-8"))
        self.header_to_parse_func = {"Online": self.mqtt_rec_online,"Quest step reached":self.mqtt_rec_step_reached,"Status":self.mqtt_rec_status,
                                     "Quest?" : self.mqtt_rec_quest_answer,
                                     } #Mapa de headers con su respectiva función de parseo
        try: ##Para que no estalle en caso de ser un mensaje fuera del protocolo
            header_known=False;
            print(msg)
            self.AGVn_rec = int((msg.split('\n', 1)[0]).split('V',1)[1])
            self.msg_rec = msg.split('\n', 1)[1]  # Me quedo con los datos del agv
            for key in self.header_to_parse_func:  # Me fijo si es alguno de los headers esperados, lo parsea con su respectiva función
                if self.msg_rec.startswith(key):
                    msg_error = self.header_to_parse_func[key]()
                    header_known=True;
            if not header_known:
                self.log.appendPlainText("Recieved a msg with an unknown header" + self.msg_rec);
            if msg_error:
                self.log.appendPlainText(msg_error)
        except Exception as e:
            print(e)

    #### Funciones útiles
    def update_map(self):
        prev, next, distance = self.agv_status_dict[1].get_agv_pos_nodes()
        self.map.update_agv_pos(1, prev, next, distance)
        self.canvas.draw_idle()
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
        dict= {'B':"Bp",'H':"Hc",'D':"De",'N':"No"}
        return dict[char.upper()]
    #### Funciones de parseo de comandos ###
    def mqtt_rec_online(self):
        self.agv_status_dict[self.AGVn_rec] = AGV_status(self.AGVn_rec)
        self.log.appendPlainText("AGV " + str(self.AGVn_rec) + ": " + "Online")
    def mqtt_rec_step_reached(self):
        if self.agv_status_dict[self.AGVn_rec].in_mission:
            self.agv_status_dict[self.AGVn_rec].mission_step_reached()
            self.log.appendPlainText("AGV " + str(self.AGVn_rec) + ": " + "Step reached")
        else:
            print("Error")
    def mqtt_rec_status(self):
        dist_trav=search("Distance: {:d}", self.msg_rec)
        if dist_trav: #Si se recibió una distancia
            self.agv_status_dict[self.AGVn_rec].distanceTravelled = dist_trav[0]
        bat_lev_rec=search("BatVolt: {:d}", self.msg_rec)
        if bat_lev_rec: #Si se recibió una tensión
            batLevel = float(bat_lev_rec[0]) / 100.0;
            self.battery.setBatLevel(batLevel)
        self.log.appendPlainText("AGV " + str(self.AGVn_rec) + ": " + "Status update")
    def mqtt_rec_quest_answer(self):
        if "Yes" in self.msg_rec:
            self.agv_status_dict[self.AGVn_rec].in_mission = True;
            self.log.appendPlainText("AGV " + str(self.AGVn_rec) + ": " + "Mission accepted")
        elif "No" in self.msg_rec:
            self.agv_status_dict[self.AGVn_rec].in_mission = False;
            self.log.appendPlainText("AGV " + str(self.AGVn_rec) + ": " + "Mission denied")
        else:
            return "Expected Yes or No after the header"
    #### Funciones llamadas por comandos ###
    def setBat(self):
        res = parse("B {:d}", self.last_command)
        bvolt= res[0] / 100;
        self.battery.setBatLevel(bvolt);
        return True;
    def setVel(self):
        res = parse("S {:d} {:d}", self.last_command)
        msg_to_send = "Fixed speed\n" + str(res[0])+ " " + str(res[1]);
        self.mqttClient.publish("AGV1",msg_to_send)
        return True;
    def set_position(self):
        res = parse("SetPos {:d}", self.last_command)
        self.agv_status_dict[1].set_pos( res[0])
        self.update_map()
        return True;
    def start_mission(self):
        res = search("SM {:d}", self.last_command)
        steps_str,node_path,dist_list = self.map.get_path(self.agv_status_dict[1].in_node, res[0])
        msg_to_send= "Quest?\n" + "No"+self.gen_mission_block(steps_str, dist_list)+"No"
        self.agv_status_dict[1].new_mission([node_path],[dist_list], ["None", "None"]) #Las IBE son none por ser una misión simple
        self.mqttClient.publish("AGV1", msg_to_send)
        self.log.appendPlainText("New mission:" + steps_str)
        return True;
    def start_long_mission(self):
        IBE = re.findall("[HhBbNnDd]", self.last_command)                   ##Letras que indican IBE
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
        self.mqttClient.publish("AGV1", "Quest?\n" +msg_to_send)
        self.log.appendPlainText("New mission: " + msg_to_send)
        return True;
    def continueMission(self):
        self.mqttClient.publish("AGV1", "Continue")
        self.agv_status_dict[1].continue_mission()
        return True;
