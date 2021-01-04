from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
import sys
from ui_main import Ui_MainWindow
import paho.mqtt.client as mqtt


def level_to_volt(level):
    voltage = 11.4;
    voltOfCharge = {100: 12.73, 90: 12.62, 80: 12.5, 70: 12.37, 60: 12.24, 50: 12.1, 40: 11.96, 30: 11.81,
                         20: 11.66, 10: 11.51}
    for key in voltOfCharge:
        if (key <= level):
            if key<100:
                voltage = (level % 10) / 10 * (voltOfCharge[key + 10] - voltOfCharge[key]) + voltOfCharge[key]
            else:
                voltage = voltOfCharge[key]
            break
    return voltage

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mqttClient = mqtt.Client("tito")  # create new instance
        self.mqttClient.on_message = self.parse_mqtt_msg
        self.mqttClient.connect("localhost")  # connect to broker
        self.mqttClient.subscribe("AGV1")
        self.destination="Houston"
        self.mqttClient.loop_start()

        self.ui.but_accept_mission.clicked.connect(lambda : self.send_mqtt_msg("Quest?\nYes"))
        self.ui.but_emergency.clicked.connect(lambda: self.send_mqtt_msg("Emergency"))
        self.ui.but_step_reached.clicked.connect(lambda: self.send_mqtt_msg("Quest step reached"))
        self.ui.but_IBE.clicked.connect(lambda: self.send_mqtt_msg("Interblock Event"))
        self.ui.but_resumed.clicked.connect(lambda: self.send_mqtt_msg("Resumed"))
        self.ui.but_error.clicked.connect(lambda: self.send_mqtt_msg("Error"))
        self.ui.but_mission_paused.clicked.connect(lambda: self.send_mqtt_msg("Mission paused"))
        self.ui.but_mission_aborted.clicked.connect(lambda: self.send_mqtt_msg("Mission aborted"))

        self.ui.but_agv_status.clicked.connect(self.send_status)

        self.show()
    def parse_mqtt_msg(self,client, userdata, message):
        msg = str(message.payload.decode("utf-8"))
        self.ui.log.append(msg);
    def send_status(self):
        msg="Status\n"
        count=0;
        batVolt=level_to_volt(self.ui.bat_box.value())
        if self.ui.dist_chkbox.isChecked():
            msg += "Distance: " +str(int(self.ui.dist_box.value()))
            if self.ui.bat_chkbox.isChecked():
                msg += "\n" + "BatVolt: "+str(int(batVolt*100))
        elif self.ui.bat_chkbox.isChecked():
            msg += "BatVolt: " + str(int(batVolt*100))
        self.send_mqtt_msg(msg)
    def send_mqtt_msg(self,msg):
        self.mqttClient.publish(self.destination,"AGV1\n"+msg)
        self.ui.log.append("Sent:" +msg);

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())