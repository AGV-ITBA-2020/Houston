################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
from parse import *
from MapManager import MapManager
import re
import paho.mqtt.client as mqtt
from AGV_status import AGV_status
from Battery import Battery


# GUI FILE
from app_modules import *

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
        self.mqttClient.on_message = self.parse_msg
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
    def parse_msg(self,client, userdata, message): ##Parseo de mensajes de MQTT
        msg=str(message.payload.decode("utf-8"))
        AGVn = int((msg.split('\n', 1)[0]).split('V',1)[1])
        msg = msg.split('\n', 1)[1]  # Me quedo con los datos del agv
        #self.log.append("AGV " + str(AGVn) + ": " + msg)
        if msg == "Online":
            self.agv_status_dict[AGVn] = AGV_status(AGVn)
            self.update_map()
            self.log.appendPlainText("AGV " + str(AGVn) + ": " + "Online")
        elif msg=="Quest step reached":
            if self.agv_status_dict[AGVn].in_mission:
                self.agv_status_dict[AGVn].mission_step_reached()
                self.update_map()
                self.log.appendPlainText("AGV " + str(AGVn) + ": " + "Step reached")
            else:
                print("Error")
        elif "Status" in msg:
            self.agv_status_dict[AGVn].distanceTravelled = search("Distance: {:d}", msg)[0]
            batLevel= float(search("BatVolt: {:d}", msg)[0])/100.0;
            #self.log.appendPlainText("AGV " + str(AGVn) + ": " + "Battery: " + str(batLevel)+"V")
            self.update_map()
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


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.setWindowIcon(QtGui.QIcon("AGV.png"))
        self.ui.setupUi(self)
        self.add_map_plot()
        self.ui.battery = Battery();
        self.ui.layout_plot_battery.addWidget(self.ui.battery)
        self.backend = Backend(self.ui.log,self.ui.canvas,self.ui.battery)
        self.ui.command_entry.editingFinished.connect(self.enter_command)
        self.add_agv_data()
        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('ITBAGV')
        UIFunctions.labelTitle(self, 'ITBAGV')
        UIFunctions.labelDescription(self, 'Houston')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Home", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True) #cil-map puede servir
        UIFunctions.addNewMenu(self, "System data", "btn_system_data", "url(:/16x16/icons/16x16/cil-chart-line.png)", True)
        UIFunctions.addNewMenu(self, "Settings", "btn_settings", "url(:/16x16/icons/16x16/cil-settings.png)", False)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "Ho", "", True)
        ## ==> END ##


        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################




        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################



        ## ==> QTableWidget RARAMETERS
        ########################################################################
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ## ==> END ##



        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
    def add_map_plot(self):
        ##Agrego el canvas de matplotlib que no se puede poner desde qt
        self.ui.figure = plt.figure()
        self.ui.canvas = FigureCanvas(self.ui.figure)
        self.ui.canvas.draw_idle()
        self.ui.verlayout_plot_panel = QVBoxLayout(self.ui.plot_frame)
        self.ui.nt = NavigationToolbar(self.ui.canvas, self)
        self.ui.nt.setMaximumSize(QSize(16777215, 65))
        self.ui.verlayout_plot_panel.addWidget(self.ui.nt)
        self.ui.verlayout_plot_panel.addWidget(self.ui.canvas)
        self.ui.canvas.draw_idle()

    def add_agv_data(self):
        # self.ui.agv_design_plot_frame.setStyleSheet(u"background-image: url(AGV.png);\n"
        #                                          "background-position: center;\n"
        #                                          "background-repeat: no-repeat;")
        self.ui.aux=2
    def enter_command(self):
        retVal=self.backend.parse_cmd(self.ui.command_entry.text())
        self.ui.command_entry.clear()
        if  retVal == False: #Si no se reconoció ningun comando, se comunica.
            self.ui.log.appendPlainText("Invalid Command")
    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE NEW USER
        if btnWidget.objectName() == "btn_system_data":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_data)
            UIFunctions.resetStyle(self, "btn_system_data")
            UIFunctions.labelPage(self, "System data")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_settings":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)
            UIFunctions.resetStyle(self, "btn_settings")
            UIFunctions.labelPage(self, "Settings")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    # def keyPressEvent(self, event):
    #     print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        Height=str(self.height())
        #print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    # sys._excepthook = sys.excepthook
    # def my_exception_hook(exctype, value, traceback):
    #     # Print the error and traceback
    #     print(exctype, value, traceback)
    #     # Call the normal Exception hook after
    #     sys._excepthook(exctype, value, traceback)
    #     sys.exit(1)
    #
    #
    # # Set the exception hook to our wrapping function
    # sys.excepthook = my_exception_hook
    # try:
    #     sys.exit(app.exec_())
    # except:
    #     print("Exiting")
    sys.exit(app.exec_())
