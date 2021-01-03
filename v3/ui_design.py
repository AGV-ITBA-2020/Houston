# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designzMtmBc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1138, 812)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1101, 631))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(50, 10, 1091, 631))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_11)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 60, 251, 541))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.log = QTextEdit(self.frame_4)
        self.log.setObjectName(u"log")
        self.log.setGeometry(QRect(10, 70, 231, 461))
        self.log.setReadOnly(True)
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(10, 10, 221, 31))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_11)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(280, 60, 581, 551))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 10, 541, 41))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.plot_frame = QFrame(self.frame_3)
        self.plot_frame.setObjectName(u"plot_frame")
        self.plot_frame.setGeometry(QRect(10, 60, 551, 481))
        self.plot_frame.setFrameShape(QFrame.StyledPanel)
        self.plot_frame.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.frame_11)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(890, 110, 181, 341))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 60, 161, 41))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.agv_data_flag_in_mission = QLabel(self.frame_6)
        self.agv_data_flag_in_mission.setObjectName(u"agv_data_flag_in_mission")
        self.agv_data_flag_in_mission.setGeometry(QRect(20, 20, 14, 14))
        self.agv_data_flag_in_mission.setPixmap(QPixmap(u"../v2/led-red-on.png"))
        self.agv_data_flag_in_mission.setScaledContents(True)
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(40, 220, 120, 80))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frame_8)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 121, 81))
        self.layout_plot_battery = QVBoxLayout(self.verticalLayoutWidget)
        self.layout_plot_battery.setObjectName(u"layout_plot_battery")
        self.layout_plot_battery.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(20, 10, 151, 31))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(160, 630, 751, 81))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.command_entry = QLineEdit(self.frame_2)
        self.command_entry.setObjectName(u"command_entry")
        self.command_entry.setGeometry(QRect(30, 40, 701, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.agv_data_flag_in_mission.setText("")
    # retranslateUi

