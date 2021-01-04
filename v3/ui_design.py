# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designrWxSEP.ui'
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
        MainWindow.resize(1280, 800)
        MainWindow.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(94, 94, 94);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1280, 800))
        self.frame.setMinimumSize(QSize(1280, 800))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_info = QFrame(self.frame)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_info)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_log = QFrame(self.frame_info)
        self.frame_log.setObjectName(u"frame_log")
        self.frame_log.setMinimumSize(QSize(0, 0))
        self.frame_log.setMaximumSize(QSize(300, 16777215))
        self.frame_log.setFrameShape(QFrame.StyledPanel)
        self.frame_log.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_log)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_9 = QFrame(self.frame_log)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 40))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.icon_log = QLabel(self.frame_9)
        self.icon_log.setObjectName(u"icon_log")
        self.icon_log.setMaximumSize(QSize(12, 12))
        self.icon_log.setPixmap(QPixmap(u"icons/16x16/cil-comment-bubble.png"))
        self.icon_log.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.icon_log)

        self.title_log = QLabel(self.frame_9)
        self.title_log.setObjectName(u"title_log")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.title_log.setFont(font)
        self.title_log.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.title_log)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.log = QTextEdit(self.frame_log)
        self.log.setObjectName(u"log")
        self.log.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.log)


        self.horizontalLayout.addWidget(self.frame_log)

        self.frame_navigator = QFrame(self.frame_info)
        self.frame_navigator.setObjectName(u"frame_navigator")
        self.frame_navigator.setMinimumSize(QSize(600, 0))
        self.frame_navigator.setFrameShape(QFrame.StyledPanel)
        self.frame_navigator.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_navigator)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_13 = QFrame(self.frame_navigator)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 40))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.icon_log_4 = QLabel(self.frame_13)
        self.icon_log_4.setObjectName(u"icon_log_4")
        self.icon_log_4.setMaximumSize(QSize(12, 12))
        self.icon_log_4.setPixmap(QPixmap(u"icons/16x16/cil-map.png"))
        self.icon_log_4.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.icon_log_4)

        self.title_log_4 = QLabel(self.frame_13)
        self.title_log_4.setObjectName(u"title_log_4")
        self.title_log_4.setFont(font)
        self.title_log_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.title_log_4)


        self.verticalLayout_4.addWidget(self.frame_13)

        self.plot_frame = QFrame(self.frame_navigator)
        self.plot_frame.setObjectName(u"plot_frame")
        self.plot_frame.setFrameShape(QFrame.StyledPanel)
        self.plot_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.plot_frame)


        self.horizontalLayout.addWidget(self.frame_navigator)

        self.frame_flags = QFrame(self.frame_info)
        self.frame_flags.setObjectName(u"frame_flags")
        self.frame_flags.setMinimumSize(QSize(200, 0))
        self.frame_flags.setFrameShape(QFrame.StyledPanel)
        self.frame_flags.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_flags)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_12 = QFrame(self.frame_flags)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 40))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.icon_log_3 = QLabel(self.frame_12)
        self.icon_log_3.setObjectName(u"icon_log_3")
        self.icon_log_3.setMaximumSize(QSize(12, 12))
        self.icon_log_3.setPixmap(QPixmap(u"icons/Others/AGV.png"))
        self.icon_log_3.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.icon_log_3)

        self.title_log_3 = QLabel(self.frame_12)
        self.title_log_3.setObjectName(u"title_log_3")
        self.title_log_3.setFont(font)
        self.title_log_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.title_log_3)


        self.verticalLayout_5.addWidget(self.frame_12)

        self.frame_6 = QFrame(self.frame_flags)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_14 = QFrame(self.frame_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 40))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.agv_data_flag_in_mission = QLabel(self.frame_14)
        self.agv_data_flag_in_mission.setObjectName(u"agv_data_flag_in_mission")
        self.agv_data_flag_in_mission.setMaximumSize(QSize(12, 12))
        self.agv_data_flag_in_mission.setPixmap(QPixmap(u"icons/led-red-on.png"))
        self.agv_data_flag_in_mission.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.agv_data_flag_in_mission)

        self.title_log_5 = QLabel(self.frame_14)
        self.title_log_5.setObjectName(u"title_log_5")
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setWeight(50)
        self.title_log_5.setFont(font1)
        self.title_log_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.title_log_5)


        self.verticalLayout_6.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 40))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.agv_data_flag_mission_paused = QLabel(self.frame_15)
        self.agv_data_flag_mission_paused.setObjectName(u"agv_data_flag_mission_paused")
        self.agv_data_flag_mission_paused.setMaximumSize(QSize(12, 12))
        self.agv_data_flag_mission_paused.setPixmap(QPixmap(u"icons/led-red-on.png"))
        self.agv_data_flag_mission_paused.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.agv_data_flag_mission_paused)

        self.title_log_6 = QLabel(self.frame_15)
        self.title_log_6.setObjectName(u"title_log_6")
        self.title_log_6.setFont(font1)
        self.title_log_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.title_log_6)


        self.verticalLayout_6.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 40))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.agv_data_flag_waiting_for_IBE = QLabel(self.frame_16)
        self.agv_data_flag_waiting_for_IBE.setObjectName(u"agv_data_flag_waiting_for_IBE")
        self.agv_data_flag_waiting_for_IBE.setMaximumSize(QSize(12, 12))
        self.agv_data_flag_waiting_for_IBE.setPixmap(QPixmap(u"icons/led-red-on.png"))
        self.agv_data_flag_waiting_for_IBE.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.agv_data_flag_waiting_for_IBE)

        self.title_log_7 = QLabel(self.frame_16)
        self.title_log_7.setObjectName(u"title_log_7")
        self.title_log_7.setFont(font1)
        self.title_log_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.title_log_7)


        self.verticalLayout_6.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_6)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 40))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.agv_data_flag_emergency = QLabel(self.frame_17)
        self.agv_data_flag_emergency.setObjectName(u"agv_data_flag_emergency")
        self.agv_data_flag_emergency.setMaximumSize(QSize(12, 12))
        self.agv_data_flag_emergency.setPixmap(QPixmap(u"icons/led-red-on.png"))
        self.agv_data_flag_emergency.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.agv_data_flag_emergency)

        self.title_log_8 = QLabel(self.frame_17)
        self.title_log_8.setObjectName(u"title_log_8")
        self.title_log_8.setFont(font1)
        self.title_log_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.title_log_8)


        self.verticalLayout_6.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_6)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 40))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.agv_data_flag_error = QLabel(self.frame_18)
        self.agv_data_flag_error.setObjectName(u"agv_data_flag_error")
        self.agv_data_flag_error.setMaximumSize(QSize(12, 12))
        self.agv_data_flag_error.setPixmap(QPixmap(u"icons/led-red-on.png"))
        self.agv_data_flag_error.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.agv_data_flag_error)

        self.title_log_9 = QLabel(self.frame_18)
        self.title_log_9.setObjectName(u"title_log_9")
        self.title_log_9.setFont(font1)
        self.title_log_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.title_log_9)


        self.verticalLayout_6.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_6)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 40))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.agv_data_flag_waiting_for_continue = QLabel(self.frame_19)
        self.agv_data_flag_waiting_for_continue.setObjectName(u"agv_data_flag_waiting_for_continue")
        self.agv_data_flag_waiting_for_continue.setMaximumSize(QSize(12, 12))
        self.agv_data_flag_waiting_for_continue.setPixmap(QPixmap(u"icons/led-red-on.png"))
        self.agv_data_flag_waiting_for_continue.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.agv_data_flag_waiting_for_continue)

        self.title_log_10 = QLabel(self.frame_19)
        self.title_log_10.setObjectName(u"title_log_10")
        self.title_log_10.setFont(font1)
        self.title_log_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.title_log_10)


        self.verticalLayout_6.addWidget(self.frame_19)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_flags)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 150))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.layout_plot_battery = QVBoxLayout(self.frame_8)
        self.layout_plot_battery.setObjectName(u"layout_plot_battery")

        self.verticalLayout_5.addWidget(self.frame_8)


        self.horizontalLayout.addWidget(self.frame_flags)


        self.verticalLayout.addWidget(self.frame_info)

        self.frame_command = QFrame(self.frame)
        self.frame_command.setObjectName(u"frame_command")
        self.frame_command.setMinimumSize(QSize(0, 100))
        self.frame_command.setMaximumSize(QSize(16777215, 16777215))
        self.frame_command.setFrameShape(QFrame.StyledPanel)
        self.frame_command.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_command)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_11 = QFrame(self.frame_command)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 40))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.icon_log_2 = QLabel(self.frame_11)
        self.icon_log_2.setObjectName(u"icon_log_2")
        self.icon_log_2.setMaximumSize(QSize(12, 12))
        self.icon_log_2.setPixmap(QPixmap(u"icons/16x16/cil-terminal.png"))
        self.icon_log_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.icon_log_2)

        self.title_command = QLabel(self.frame_11)
        self.title_command.setObjectName(u"title_command")
        self.title_command.setFont(font)
        self.title_command.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.title_command)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.command_entry = QLineEdit(self.frame_command)
        self.command_entry.setObjectName(u"command_entry")

        self.verticalLayout_2.addWidget(self.command_entry)


        self.verticalLayout.addWidget(self.frame_command)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.icon_log.setText("")
        self.title_log.setText(QCoreApplication.translate("MainWindow", u"Log", None))
        self.icon_log_4.setText("")
        self.title_log_4.setText(QCoreApplication.translate("MainWindow", u"Navigator", None))
        self.icon_log_3.setText("")
        self.title_log_3.setText(QCoreApplication.translate("MainWindow", u"AGV Status Flags", None))
        self.agv_data_flag_in_mission.setText("")
        self.title_log_5.setText(QCoreApplication.translate("MainWindow", u"In Mission", None))
        self.agv_data_flag_mission_paused.setText("")
        self.title_log_6.setText(QCoreApplication.translate("MainWindow", u"Mission paused", None))
        self.agv_data_flag_waiting_for_IBE.setText("")
        self.title_log_7.setText(QCoreApplication.translate("MainWindow", u"Waiting for IBE", None))
        self.agv_data_flag_emergency.setText("")
        self.title_log_8.setText(QCoreApplication.translate("MainWindow", u"Emergency", None))
        self.agv_data_flag_error.setText("")
        self.title_log_9.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.agv_data_flag_waiting_for_continue.setText("")
        self.title_log_10.setText(QCoreApplication.translate("MainWindow", u"Wait for continue", None))
        self.icon_log_2.setText("")
        self.title_command.setText(QCoreApplication.translate("MainWindow", u"Command Line", None))
        self.command_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Command to send...", None))
    # retranslateUi

