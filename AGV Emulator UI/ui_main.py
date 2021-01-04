# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Agv EmulatorzaZvko.ui'
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
        MainWindow.resize(974, 680)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 950, 640))
        self.frame.setMinimumSize(QSize(950, 640))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.but_IBE = QPushButton(self.frame_2)
        self.but_IBE.setObjectName(u"but_IBE")

        self.gridLayout.addWidget(self.but_IBE, 2, 1, 1, 1)

        self.but_mission_aborted = QPushButton(self.frame_2)
        self.but_mission_aborted.setObjectName(u"but_mission_aborted")

        self.gridLayout.addWidget(self.but_mission_aborted, 3, 1, 1, 1)

        self.but_error = QPushButton(self.frame_2)
        self.but_error.setObjectName(u"but_error")

        self.gridLayout.addWidget(self.but_error, 2, 0, 1, 1)

        self.but_mission_paused = QPushButton(self.frame_2)
        self.but_mission_paused.setObjectName(u"but_mission_paused")

        self.gridLayout.addWidget(self.but_mission_paused, 3, 0, 1, 1)

        self.but_emergency = QPushButton(self.frame_2)
        self.but_emergency.setObjectName(u"but_emergency")

        self.gridLayout.addWidget(self.but_emergency, 1, 0, 1, 1)

        self.but_step_reached = QPushButton(self.frame_2)
        self.but_step_reached.setObjectName(u"but_step_reached")

        self.gridLayout.addWidget(self.but_step_reached, 0, 1, 1, 1)

        self.but_accept_mission = QPushButton(self.frame_2)
        self.but_accept_mission.setObjectName(u"but_accept_mission")

        self.gridLayout.addWidget(self.but_accept_mission, 0, 0, 1, 1)

        self.but_resumed = QPushButton(self.frame_2)
        self.but_resumed.setObjectName(u"but_resumed")

        self.gridLayout.addWidget(self.but_resumed, 1, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 200))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.but_agv_status = QPushButton(self.frame_4)
        self.but_agv_status.setObjectName(u"but_agv_status")
        self.but_agv_status.setGeometry(QRect(110, 160, 214, 23))
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(20, 20, 401, 41))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.dist_box = QDoubleSpinBox(self.frame_6)
        self.dist_box.setObjectName(u"dist_box")
        self.dist_box.setDecimals(0)
        self.dist_box.setMaximum(2000.000000000000000)

        self.horizontalLayout_3.addWidget(self.dist_box)

        self.dist_chkbox = QCheckBox(self.frame_6)
        self.dist_chkbox.setObjectName(u"dist_chkbox")
        self.dist_chkbox.setChecked(True)

        self.horizontalLayout_3.addWidget(self.dist_chkbox)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(20, 70, 401, 41))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.bat_box = QDoubleSpinBox(self.frame_7)
        self.bat_box.setObjectName(u"bat_box")
        self.bat_box.setDecimals(1)
        self.bat_box.setValue(100.000000000000000)

        self.horizontalLayout_4.addWidget(self.bat_box)

        self.bat_chkbox = QCheckBox(self.frame_7)
        self.bat_chkbox.setObjectName(u"bat_chkbox")
        self.bat_chkbox.setChecked(True)

        self.horizontalLayout_4.addWidget(self.bat_chkbox)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.log = QTextEdit(self.frame_5)
        self.log.setObjectName(u"log")
        self.log.setGeometry(QRect(10, 10, 421, 371))

        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout_2.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.but_IBE.setText(QCoreApplication.translate("MainWindow", u"IBE recieved", None))
        self.but_mission_aborted.setText(QCoreApplication.translate("MainWindow", u"Mission Abort", None))
        self.but_error.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.but_mission_paused.setText(QCoreApplication.translate("MainWindow", u"Mission paused", None))
        self.but_emergency.setText(QCoreApplication.translate("MainWindow", u"Emergency", None))
        self.but_step_reached.setText(QCoreApplication.translate("MainWindow", u"Step Reached", None))
        self.but_accept_mission.setText(QCoreApplication.translate("MainWindow", u"Accept Mission", None))
        self.but_resumed.setText(QCoreApplication.translate("MainWindow", u"Resumed", None))
        self.but_agv_status.setText(QCoreApplication.translate("MainWindow", u"AGV status", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Distancia [cm]", None))
        self.dist_chkbox.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Bater\u00eda [%]", None))
        self.bat_chkbox.setText("")
    # retranslateUi

