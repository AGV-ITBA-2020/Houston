from PySide2.QtWidgets import QProgressBar,QMessageBox
from PySide2.QtGui import QPainter,QPainterPath,QPen
from PySide2 import QtGui, QtCore
from PySide2.QtCore import Signal

OK_STYLE='''
        QProgressBar {
            border: 4px solid white;
            background-color: rgb(41, 45, 56);
            margin-top: 12px;
        }
        QProgressBar:horizontal {
            height: 60px;
            width: 120px;
            margin-right: 12px;
        }
        QProgressBar:vertical {
            height: 120px;
            width: 60px;
            margin-left: 12px;
        }
        QProgressBar::chunk {
            background-color: white;
            margin: 4px;
        }'''
WARNING_STYLE='''
        QProgressBar {
            border: 4px solid yellow;
            background-color: rgb(41, 45, 56);
            margin-top: 12px;
        }
        QProgressBar:horizontal {
            height: 60px;
            width: 120px;
            margin-right: 12px;
        }
        QProgressBar:vertical {
            height: 120px;
            width: 60px;
            margin-left: 12px;
        }
        QProgressBar::chunk {
            background-color: yellow;
            margin: 4px;
        }'''
LOW_STYLE='''
        QProgressBar {
            border: 4px solid red;
            background-color: rgb(41, 45, 56);
            margin-top: 12px;
        }
        QProgressBar:horizontal {
            height: 60px;
            width: 120px;
            margin-right: 12px;
        }
        QProgressBar:vertical {
            height: 120px;
            width: 60px;
            margin-left: 12px;
        }
        QProgressBar::chunk {
            background-color: red;
            margin: 4px;
        }'''


class Battery(QProgressBar):
    def __init__(self, *args, **kwargs):
        super(Battery, self).__init__(*args, **kwargs)
        self.setTextVisible(False)
        self.charging = False
        self.state = "Ok"; #Puede ser warning o low
        self.voltOfCharge = {100: 12.73, 90: 12.62, 80: 12.5, 70: 12.37, 60: 12.24, 50: 12.1, 40: 11.96, 30: 11.81,
                             20: 11.66, 10: 11.51}
        self.setMaximum(100)
        self.setMinimum(0)
        self.color= QtCore.Qt.white
        self.setValue(100)
        self.setStyleSheet(OK_STYLE)
    def reset(self):
        self.state = "Ok"
        self.setValue(100)
    def level_to_volt(self,level):
        voltage=11.4;
        for key in self.voltOfCharge:
            if(key<=level):
                voltage = (level%10)/10 * (self.voltOfCharge[key + 10] - self.voltOfCharge[key]) + self.voltOfCharge[key]
        return voltage
    def volt_to_level(self,volt):
        level=0;
        res = 10 ##Si la resolución de la batería es de 10

        for key in self.voltOfCharge:
            if(self.voltOfCharge[key]<=volt):
                if(res==10):
                    level=key
                if (res == 1): #No ta checkeado
                    if(key<100):
                        if(volt>self.voltOfCharge[key]):
                            level=int((volt-self.voltOfCharge[key])/(self.voltOfCharge[key+10]-self.voltOfCharge[key])*10 + key);
                        else:
                            level=key;
                    else:
                        level=100;
                break;
        return level
    def reset(self):
        self.state="Ok"
        self.setValue(100)
    def setBatLevel(self, voltage):
        b_level=self.volt_to_level(voltage)
        #if b_level <= self.value():
        self.setValue(b_level)
        if (b_level >= 50 and not self.state == "Ok"):
            self.state="Ok"
            # self.color = QtCore.Qt.white
            # self.setStyleSheet(OK_STYLE)
        if(b_level <= 30 and b_level > 15 and self.state == "Ok"):
            self.state = "Warning"
            # self.color = QtCore.Qt.yellow
            # self.setStyleSheet(WARNING_STYLE)
        if (b_level <= 15 and not self.state == "Low"):
            self.state = "Low"
            # self.color = QtCore.Qt.red
            # self.setStyleSheet(LOW_STYLE)
        self.repaint()

    def setCharging(self, state):
        self.charging = state
        self.repaint()

    def paintEvent(self, event):
        super(Battery, self).paintEvent(event)
        qp = QPainter(self)
        qp.setPen(QtCore.Qt.NoPen);
        qp.setBrush(self.color)
        w, h = self.width(), self.height()
        if self.orientation() == QtCore.Qt.Horizontal:
            qp.drawRect(w, 12 + h / 4, -12, h / 2 - 12)
            dx, dy = 0, 12
        else:
            qp.drawRect(12 + w / 4, 0, w / 2 - 12, 12)
            dx, dy = 12, 0

        qp.setPen(QtCore.Qt.gray)
        font=qp.font()
        font.setPointSize(font.pointSize()*1.5)
        qp.setFont(font)
        qp.drawText(self.rect().adjusted(dx, dy, 0, 0), QtCore.Qt.AlignCenter, self.text())
        qp.setPen(QtCore.Qt.NoPen)

        if self.charging:
            qp.setBrush(self.parent().palette().window())
            qp.setBrush(self.color)
            path = QPainterPath()
            if self.orientation() == QtCore.Qt.Horizontal:
                qp.drawRect(0, 0, 12, h)
                path.moveTo(12, h)
                path.lineTo(12, 12 + h / 3)
                path.quadTo(22, 12 + h / 3, 22, 24)
                path.lineTo(22, 14)
                path.lineTo(2, 14)
                path.lineTo(2, 24)
                path.quadTo(2, 12 + h / 3, 12, 12 + h / 3)
                path.moveTo(7, 12);
                path.lineTo(7, 0)
                path.moveTo(17, 12);
                path.lineTo(17, 0)
            else:
                qp.drawRect(0, h, w, -12)
                path.moveTo(w, h - 12)
                path.lineTo(12 + w / 3, h - 12)
                path.quadTo(12 + w / 3, h - 22, 24, h - 22)
                path.lineTo(14, h - 22)
                path.lineTo(14, h - 2)
                path.lineTo(24, h - 2)
                path.quadTo(12 + w / 3, h - 2, 12 + w / 3, h - 12)
                path.moveTo(12, h - 7);
                path.lineTo(0, h - 7)
                path.moveTo(12, h - 17);
                path.lineTo(0, h - 17)

            pen = QPen(qp.brush(), 12, QtCore.Qt.SolidLine, QtCore.Qt.SquareCap, QtCore.Qt.MiterJoin)
            qp.strokePath(path, pen)
            pen.setWidth(4);
            pen.setColor(self.color);
            qp.setPen(pen)
            #qp.setBrush(self.palette().window())
            qp.setBrush(self.color)
            qp.drawPath(path)
