from MapManager import MapManager
import re
import paho.mqtt.client as mqtt
from Battery import Battery
from AGV_status import AGV_status
from parse import *
import datetime
import copy

class Backend:
    def __init__(self,battery):
        self.map = MapManager()
        self.log = "";
        self.battery = battery;
        self.error=False;
        # Estructura de comandos aceptados por consola
        self.command_mapping = {re.compile('(SM) [0-9]*$', re.I): self.start_mission,  # Misión simple
                                re.compile('(setPos) [0-9]*$', re.I): self.set_position,  # Misión simple
                                re.compile('[s] [0-9]*$', re.I): self.setVel,
                                re.compile('[B] [0-9]*$', re.I): self.setBat, #Pone nivel de batería
                                re.compile('(LM) ([HBDN] [0-9]* )*[HBDN]$', re.I): self.start_long_mission,
                                # Misión larga: LM para indicar misión, luego serie de eventos y nodos a llegar y al final el evento final. B=button, D=delay, H=houston continue N=None
                                re.compile('[C]$', re.I): self.continueMission,
                                re.compile('[P]$', re.I): self.pauseMission,
                                re.compile('[A]$', re.I): self.abortMission
                                }
        self.mqttClient = mqtt.Client("Houston")  # create new instance
        self.mqttClient.on_message = self.parse_mqtt_msg
        self.mqttClient.connect("localhost")  # connect to broker
        self.mqttClient.subscribe("Houston")
        self.agv_status_dict = {};  # Status de los AGVs que se conecten
        self.agv_status_dict[1] = AGV_status(1)  # Para debuggear ya lo dejamos creado al agv1
        self.map.update_agv_pos(1, 1, 1, 0)

        self.map_changed= 1;
    def get_log(self):
        aux=copy.deepcopy(self.log)
        self.log=""
        return aux
    def sync_mqtt_msg_check(self):
        self.mqttClient.loop()
    def parse_cmd(self,cmd):
        self.last_command=cmd
        cmdValid=False;
        msg_error=""
        if re.compile('[R]$', re.I).match(cmd): #Si llegó un reset, lo ejecuto siempre
            self.restart()
            cmdValid = True;
        else: #Sino, depende si estoy en error o no
            for key in self.command_mapping:  #Para todos los comandos que tengo estipulados
                if key.match(cmd) and not self.error: #Solo si el cmd es lo esperado y no está el backend en estado error
                    msg_error = self.command_mapping[key]()
                    cmdValid = True;
        if not cmdValid:
            msg_error= "Unknown command: " + cmd
        return msg_error
    def parse_mqtt_msg(self,client, userdata, message): ##Parseo de mensajes de MQTT
        msg=str(message.payload.decode("utf-8"))
        self.header_to_parse_func = {"Online": self.mqtt_rec_online,"Quest step reached":self.mqtt_rec_step_reached,"Status":self.mqtt_rec_status,
                                     "Quest\n" : self.mqtt_rec_quest_answer,"Quest paused":self.mqtt_rec_pause_mission,"Resumed":self.mqtt_rec_continue,
                                     "Quest abort": self.mqtt_rec_abort,"Emergency stop": self.mqtt_rec_emergency,"Error":self.mqtt_rec_error,
                                     "Interblock event": self.mqtt_rec_IBE, "HB": self.mqtt_rec_hb,"Emergency button freed": self.mqtt_rec_emergency_but
                                     } #Mapa de headers con su respectiva función de parseo
        try: ##Para que no estalle en caso de ser un mensaje fuera del protocolo
            header_known=False;
            msg_error=""
            #print(msg)
            self.AGVn_rec = int((msg.split('\n', 1)[0]).split('V',1)[1])
            self.msg_rec = msg.split('\n', 1)[1]  # Me quedo con los datos del agv
            for key in self.header_to_parse_func:  # Me fijo si es alguno de los headers esperados, lo parsea con su respectiva función
                if self.msg_rec.startswith(key) and not self.error:
                    self.log+=(datetime.datetime.now().strftime("%H:%M:%S -"))
                    msg_error = self.header_to_parse_func[key]() #Devuelve un string del error si hubo
                    header_known=True;
            if (not header_known) and (not self.error): #Si estoy en error no voy a tomar ningún header.
                self.log+=("Recieved a msg with an unknown header" + self.msg_rec);
            elif msg_error: #Si hubo un error lógico del mensaje, se pone al backend en estado error
                self.error=True;
                self.log+=(msg_error)
        except Exception as e:
            print(e)

    #### Funciones útiles
    def check_for_map_updates(self):
        retVal=False
        if self.map_changed==1:
            self.map_changed = 0
            retVal=True;
        return retVal;

    def update_map(self):
        prev, next, distance = self.agv_status_dict[1].get_agv_pos_nodes()
        self.map.update_agv_pos(1, prev, next, distance)
        self.map_changed = 1;
    def gen_mission_block(self, steps, dists): ##Dados los steps y las distancias, genera el texto que lo representa para enviar por mqtt
        mission = "Bs" #Block start
        for i in range(int(len(steps)/2)):
            mission += dists[i] + steps[(i*2):(i*2+2)]; #Pone por ejemplo 11Fr14Sl1
        mission += "Be" #Block end
        return mission
    def IBECharToString(self, char):
        dict= {'B':"Button",'H':"Houston",'D':"Delay",'N':"None"}
        return dict[char.upper()]
    def IBEStringToChar(self, string):
        dict= {"Button":'B',"Houston":'H',"Delay":'D',"None":'N'}
        return dict[string]
    def IBECharToMQTTFormat(self, char):
        dict= {'B':"Bp",'H':"Hc",'D':"De",'N':"No"}
        return dict[char.upper()]
    def is_mission_cmd_valid(self,cmd):
        retVal= True;
        node_obj = list(map(int, re.findall(" [0-9]* ", cmd)))
        prev_node = self.agv_status_dict[1].in_node
        for i in range(len(node_obj)): ##Para cada bloque
            if (not self.map.is_node_station(node_obj[i])) or (prev_node == node_obj[i]): ##Si el nodo no es una estación o es igual al nodo anterior, hay un error en el comando
                retVal=False
            prev_node=node_obj[i]
        return retVal
    #### Funciones de parseo de comandos ###
    def mqtt_rec_hb(self):
        self.log+=("AGV " + str(self.AGVn_rec) + ": " + "HB")
    def mqtt_rec_online(self):
        self.agv_status_dict[self.AGVn_rec] = AGV_status(self.AGVn_rec)
        self.log+=("AGV " + str(self.AGVn_rec) + ": " + "Online")
        self.update_map();
    def mqtt_rec_step_reached(self):
        if self.agv_status_dict[self.AGVn_rec].in_mission:
            if not self.agv_status_dict[self.AGVn_rec].waiting_for_IBE and not self.agv_status_dict[self.AGVn_rec].paused:
                self.agv_status_dict[self.AGVn_rec].mission_step_reached()
                self.update_map();
                self.log+=("AGV " + str(self.AGVn_rec) + ": " + "Step reached")
            else:
                return "Recieved step reached when agv was in pause or emergency"
        else:
            return "AGV did not have any mission but recieved step reached"
    def mqtt_rec_status(self):
        dist_trav=search("Distance: {:d}", self.msg_rec)
        if dist_trav: #Si se recibió una distancia
            self.agv_status_dict[self.AGVn_rec].distanceTravelled = dist_trav[0]
            self.update_map();
        bat_lev_rec=search("BatVolt: {:d}", self.msg_rec)
        if bat_lev_rec: #Si se recibió una tensión
            batLevel = float(bat_lev_rec[0]) / 100.0;
            self.battery.setBatLevel(batLevel)
        self.log+=("AGV " + str(self.AGVn_rec) + ": " + "Status update")
    def mqtt_rec_quest_answer(self):
        if self.agv_status_dict[1].mission_sent == True: #Si se le había enviado una quest
            self.agv_status_dict[1].mission_sent = False;
            if "Yes" in self.msg_rec:
                self.agv_status_dict[self.AGVn_rec].in_mission = True;
                self.log+=("AGV " + str(self.AGVn_rec) + ": " + "Mission accepted")
            elif "No" in self.msg_rec:
                self.agv_status_dict[self.AGVn_rec].in_mission = False;
                self.log+=("AGV " + str(self.AGVn_rec) + ": " + "Mission denied")
            else:
                return "Expected Yes or No after the header -Quest?-"
        else:
            return "Recieved Quest answer, but never sent a mission"
    def mqtt_rec_pause_mission(self):
        if self.agv_status_dict[self.AGVn_rec].in_mission:
            if not self.agv_status_dict[self.AGVn_rec].paused:
                self.agv_status_dict[self.AGVn_rec].paused=1
            else:
                return "Recieved pause mission, but AGV was already in pause"
        else:
            return "Recieved pause mission, but AGV was not in a mission"

    def mqtt_rec_continue(self):
        if self.agv_status_dict[self.AGVn_rec].emergency:
            self.agv_status_dict[self.AGVn_rec].emergency=False
        elif self.agv_status_dict[1].paused:
            self.agv_status_dict[1].resume_mission()
        else:
            return "Recieved continue when it was not expected";

    def mqtt_rec_abort(self):
        if self.agv_status_dict[self.AGVn_rec].in_mission:
            self.agv_status_dict[self.AGVn_rec].abort_mission()
        else:
            return "Recieved abort when AGV was not in mission"
    def mqtt_rec_emergency(self):
        self.agv_status_dict[self.AGVn_rec].emergency= True;
        self.agv_status_dict[self.AGVn_rec].but_em_pressed = True;
    def mqtt_rec_emergency_but(self):
        self.agv_status_dict[self.AGVn_rec].but_em_pressed = False;
    def mqtt_rec_IBE(self):
        if self.agv_status_dict[1].waiting_for_IBE:
            if self.agv_status_dict[1].mission_IBE[self.agv_status_dict[1].currBlock] == "Button" or self.agv_status_dict[1].mission_IBE[self.agv_status_dict[1].currBlock] == "Delay":
                self.agv_status_dict[1].continue_mission()
            else:
                return "The IBE waited for was one that was not generated in the AGV, and it was recieved one from the AGV"
        else:
            return "Recieved an IBE without being waiting for it"
    def mqtt_rec_error(self):
        self.log+="AGV " + str(self.AGVn_rec) + ": " + self.msg_rec
        self.error=1;
    #### Funciones llamadas por comandos ###
    def restart(self):
        self.agv_status_dict[1] = AGV_status(1)  # Para debuggear ya lo dejamos creado al agv1
        self.map.update_agv_pos(1, 1, 1, 0)
        self.battery.reset()  # Pa que tenga 100%
        self.map_changed = 1;
        self.error = False;
        self.log+="System reset"
    def setBat(self):
        res = parse("B {:d}", self.last_command)
        bvolt= res[0] / 100;
        self.battery.setBatLevel(bvolt);
    def setVel(self):
        res = parse("S {:d} {:d}", self.last_command)
        msg_to_send = "Fixed speed\n" + str(res[0])+ " " + str(res[1]);
        self.mqttClient.publish("AGV1",msg_to_send)
    def set_position(self):
        res = parse("SetPos {:d}", self.last_command)
        self.agv_status_dict[1].set_pos( res[0])
        self.update_map()
        self.log+=("Position set")
    def start_mission(self):
        final_node = search("SM {:d}", self.last_command)[0]
        if self.map.is_node_station(final_node) and not(final_node==self.agv_status_dict[1].in_node):
            steps_str,node_path,dist_list = self.map.get_path(self.agv_status_dict[1].in_node, final_node)
            msg_to_send= "Quest?\n" + "No"+self.gen_mission_block(steps_str, dist_list)+"No"
            self.agv_status_dict[1].new_mission([node_path],[dist_list], ["None", "None"]) #Las IBE son none por ser una misión simple
            self.mqttClient.publish("AGV1", msg_to_send)
            self.agv_status_dict[1].mission_sent = True;
            self.log+=("New mission:" + steps_str)
        else:
            return "Final station for simple mission was not valid"
    def start_long_mission(self):
        IBE = re.findall("[HhBbNnDd]", self.last_command)                   ##Letras que indican IBE
        node_obj=list(map(int,re.findall(" [0-9]* ",self.last_command))) ##Lista con todos los nodos finales de bloques en formato int
        prev_node=self.agv_status_dict[1].in_node ##Variables que voy a usar en el loop. Este nodo es donde parte el agv.
        node_path_list =[]; path_dists_list = [];
        msg_to_send = self.IBECharToMQTTFormat(IBE[0])
        for n_block in range(len(node_obj)): ##Para cada bloque
            if self.map.is_node_station(node_obj[n_block]) and not (prev_node == node_obj[n_block]):
                steps_str, node_path, path_dists = self.map.get_path(prev_node, node_obj[n_block]) #Obtiene el camino más corto y guarda en las listas correspondientes
                node_path_list.append(node_path);path_dists_list.append(path_dists)
                msg_to_send += self.gen_mission_block(steps_str, path_dists)+self.IBECharToMQTTFormat(IBE[n_block+1]) #Pasa el camino del grafo al formato de internet, cierra el bloque y agrega el texto del IBE que va en el msg
                prev_node=node_obj[n_block]
            else:
                return "Structure of long mission was not valid"
        IBE_list = [self.IBECharToString(i) for i in IBE]               ##Se pasan letras que significan IBE a palabras para la lógica de misión
        self.agv_status_dict[1].new_mission(node_path_list, path_dists_list,IBE_list)  # Las IBE son none por ser una misión simple
        self.mqttClient.publish("AGV1", "Quest?\n" +msg_to_send)
        self.agv_status_dict[1].mission_sent = True;
        self.log+="New mission: " + msg_to_send
    def continueMission(self):

        if self.agv_status_dict[1].paused:
            self.agv_status_dict[1].resume_mission()
        elif self.agv_status_dict[1].waiting_for_IBE and self.agv_status_dict[1].mission_IBE[self.agv_status_dict[1].currBlock] == "Houston":
            self.agv_status_dict[1].continue_mission()
        elif self.agv_status_dict[1].emergency and (not self.agv_status_dict[1].but_em_pressed):
            self.agv_status_dict[1].emergency=False
        else:
            return "Continue ignored: there was not anything to continue";
        self.mqttClient.publish("AGV1", "Continue")
        self.log+=("Houston Continue")

    def pauseMission(self):
        if self.agv_status_dict[self.AGVn_rec].in_mission:
            if not self.agv_status_dict[self.AGVn_rec].paused:
                self.agv_status_dict[self.AGVn_rec].paused = 1
            else:
                return "Recieved pause mission, but AGV was already in pause"
        else:
            return "Recieved pause mission, but AGV was not in a mission"
        self.mqttClient.publish("AGV1", "Pause")
        self.log+=("Houston Pause")

    def abortMission(self):
        if self.agv_status_dict[self.AGVn_rec].in_mission:
            self.agv_status_dict[self.AGVn_rec].abort_mission()
        else:
            return "Recieved abort when AGV was not in mission"
        self.mqttClient.publish("AGV1", "Quest abort")
        self.log+="Houston Abort"
