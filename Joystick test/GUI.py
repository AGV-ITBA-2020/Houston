from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from enum import Enum
from NetworkManager import NetworkManager
import paho.mqtt.client as mqtt

class Direction(Enum):
    Left = 0
    Right = 1
    Up = 2
    Down = 3

class Joystick(QWidget):
    def __init__(self, parent=None):
        super(Joystick, self).__init__(parent)
        self.client = mqtt.Client("xd")  # create new instance
        self.client.connect("localhost") #connect to broker
        self.client.loop_start()
        self.setMinimumSize(400, 400)
        self.movingOffset = QPointF(0, 0)
        self.grabCenter = False
        self.__maxDistance = 50
        self.nm=NetworkManager()
        self.nm.set_read_callback(self.recvMsg)
    def recvMsg(self,AGVNum,msg):
        ##print(self.lastMsg) ##Se printea lo que se le va a enviar al agv
        self.msg=msg
    def paintEvent(self, event):
        painter = QPainter(self)
        bounds = QRectF(-self.__maxDistance, -self.__maxDistance, self.__maxDistance * 2, self.__maxDistance * 2).translated(self._center())
        painter.drawEllipse(bounds)
        painter.setBrush(Qt.black)
        painter.drawEllipse(self._centerEllipse())

    def _centerEllipse(self):
        if self.grabCenter:
            return QRectF(-20, -20, 40, 40).translated(self.movingOffset)
        return QRectF(-20, -20, 40, 40).translated(self._center())

    def _center(self):
        return QPointF(self.width()/2, self.height()/2)


    def _boundJoystick(self, point):
        limitLine = QLineF(self._center(), point)
        if (limitLine.length() > self.__maxDistance):
            limitLine.setLength(self.__maxDistance)
        return limitLine.p2()

    def joystickDirection(self):
        if not self.grabCenter:
            return 0
        normVector = QLineF(self._center(), self.movingOffset)
        currentDistance = normVector.length()
        self.angle = normVector.angle()
        self.distance = min(currentDistance / self.__maxDistance, 1.0)
        if(self.angle<0 or self.angle>180):
            self.angSpeed=0;
            self.linSpeed = 0;
        else:
            self.angSpeed =int((90-self.angle)/9); #Así va entre -10 y 10
           # self.linSpeed = int(self.distance*10);
            self.linSpeed = int(-normVector.dy()*10 / self.__maxDistance );
        #print(self.linSpeed)


    def mousePressEvent(self, ev):
        self.grabCenter = self._centerEllipse().contains(ev.pos())
        return super().mousePressEvent(ev)

    def mouseReleaseEvent(self, event):
        self.grabCenter = False
        self.movingOffset = QPointF(0, 0)
        self.update()

    def mouseMoveEvent(self, event):
        if self.grabCenter:
            self.movingOffset = self._boundJoystick(event.pos())
            self.update()
            self.joystickDirection()
            self.client.publish("AGV1", "Fixed speed\n"+str(self.linSpeed)+" "+ str(self.angSpeed))
            #print("linSpeed" + str(self.linSpeed)+"angSpeed" +str(self.angSpeed))

if __name__ == '__main__':
    # Create main application window
    app = QApplication([])
    app.setStyle(QStyleFactory.create("Cleanlooks"))
    mw = QMainWindow()
    mw.setWindowTitle('Joystick example')

    # Create and set widget layout
    # Main widget container
    cw = QWidget()
    ml = QGridLayout()
    cw.setLayout(ml)
    mw.setCentralWidget(cw)

    # Create joystick
    joystick = Joystick()

    # ml.addLayout(joystick.get_joystick_layout(),0,0)
    ml.addWidget(joystick,0,0)

    mw.show()

    ## Start Qt event loop unless running in interactive mode or using pyside.
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QApplication.instance().exec_()