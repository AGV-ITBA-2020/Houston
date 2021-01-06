# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designrRtyKo.ui'
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
        MainWindow.resize(1284, 809)
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
        self.frame_info.setEnabled(True)
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
        self.stackedWidget = QStackedWidget(self.frame_log)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.log_page = QWidget()
        self.log_page.setObjectName(u"log_page")
        self.frame_2 = QFrame(self.log_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, -10, 280, 391))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 50))
        self.frame_9.setMaximumSize(QSize(16777215, 50))
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

        self.but_back_to_missions = QPushButton(self.frame_9)
        self.but_back_to_missions.setObjectName(u"but_back_to_missions")
        self.but_back_to_missions.setMaximumSize(QSize(25, 25))
        self.but_back_to_missions.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/16x16/cil-screen-desktop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_back_to_missions.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.but_back_to_missions)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.log = QTextEdit(self.frame_2)
        self.log.setObjectName(u"log")
        self.log.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.log)

        self.stackedWidget.addWidget(self.log_page)
        self.main_buttons_page = QWidget()
        self.main_buttons_page.setObjectName(u"main_buttons_page")
        self.frame_3 = QFrame(self.main_buttons_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(-10, -10, 291, 741))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_20 = QFrame(self.frame_3)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 50))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.icon_log_5 = QLabel(self.frame_20)
        self.icon_log_5.setObjectName(u"icon_log_5")
        self.icon_log_5.setMaximumSize(QSize(12, 12))
        self.icon_log_5.setPixmap(QPixmap(u"icons/16x16/cil-screen-desktop.png"))
        self.icon_log_5.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.icon_log_5)

        self.title_log_11 = QLabel(self.frame_20)
        self.title_log_11.setObjectName(u"title_log_11")
        self.title_log_11.setFont(font)
        self.title_log_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.title_log_11)

        self.but_select_log = QPushButton(self.frame_20)
        self.but_select_log.setObjectName(u"but_select_log")
        self.but_select_log.setMaximumSize(QSize(25, 25))
        self.but_select_log.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/16x16/cil-chat-bubble.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_select_log.setIcon(icon1)

        self.horizontalLayout_12.addWidget(self.but_select_log)


        self.verticalLayout_7.addWidget(self.frame_20)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.but_reset = QPushButton(self.frame_4)
        self.but_reset.setObjectName(u"but_reset")
        self.but_reset.setGeometry(QRect(90, 610, 60, 24))
        self.but_reset.setMaximumSize(QSize(60, 16777215))
        self.but_reset.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/16x16/cil-power-standby.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_reset.setIcon(icon2)
        self.but_pause_or_continue = QPushButton(self.frame_4)
        self.but_pause_or_continue.setObjectName(u"but_pause_or_continue")
        self.but_pause_or_continue.setGeometry(QRect(60, 110, 121, 24))
        self.but_pause_or_continue.setMaximumSize(QSize(16777215, 16777215))
        self.but_pause_or_continue.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(179, 179, 179);\n"
"	border: 2px solid rgb(179, 179, 179);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/16x16/cil-media-pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_pause_or_continue.setIcon(icon3)
        self.but_new_mission = QPushButton(self.frame_4)
        self.but_new_mission.setObjectName(u"but_new_mission")
        self.but_new_mission.setGeometry(QRect(50, 40, 141, 21))
        self.but_new_mission.setMaximumSize(QSize(16777215, 16777215))
        self.but_new_mission.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(179, 179, 179);\n"
"	border: 2px solid rgb(179, 179, 179);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icons/16x16/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_new_mission.setIcon(icon4)
        self.but_new_mission.setIconSize(QSize(20, 20))
        self.but_abort_mission = QPushButton(self.frame_4)
        self.but_abort_mission.setObjectName(u"but_abort_mission")
        self.but_abort_mission.setGeometry(QRect(60, 180, 121, 24))
        self.but_abort_mission.setMaximumSize(QSize(16777215, 16777215))
        self.but_abort_mission.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(179, 179, 179);\n"
"	border: 2px solid rgb(179, 179, 179);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icons/16x16/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_abort_mission.setIcon(icon5)

        self.verticalLayout_7.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.main_buttons_page)
        self.mission_page = QWidget()
        self.mission_page.setObjectName(u"mission_page")
        self.frame_5 = QFrame(self.mission_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, -10, 274, 731))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_21 = QFrame(self.frame_5)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 50))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.icon_log_6 = QLabel(self.frame_21)
        self.icon_log_6.setObjectName(u"icon_log_6")
        self.icon_log_6.setMaximumSize(QSize(12, 12))
        self.icon_log_6.setPixmap(QPixmap(u"icons/16x16/cil-screen-desktop.png"))
        self.icon_log_6.setScaledContents(True)

        self.horizontalLayout_13.addWidget(self.icon_log_6)

        self.title_log_12 = QLabel(self.frame_21)
        self.title_log_12.setObjectName(u"title_log_12")
        self.title_log_12.setFont(font)
        self.title_log_12.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.title_log_12)


        self.verticalLayout_8.addWidget(self.frame_21)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(250, 660))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 50))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_11)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.IBE_1 = QComboBox(self.frame_11)
        self.IBE_1.addItem("")
        self.IBE_1.addItem("")
        self.IBE_1.addItem("")
        self.IBE_1.setObjectName(u"IBE_1")
        font1 = QFont()
        font1.setStrikeOut(False)
        self.IBE_1.setFont(font1)
        self.IBE_1.setMouseTracking(False)
        self.IBE_1.setAutoFillBackground(True)
        self.IBE_1.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.IBE_1.setMaxVisibleItems(4)
        self.IBE_1.setFrame(True)

        self.horizontalLayout_3.addWidget(self.IBE_1)


        self.verticalLayout_10.addWidget(self.frame_11)

        self.frame_22 = QFrame(self.frame_10)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_22)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 50))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_24)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 20, 55, 16))
        self.but_new_mission_steps = QPushButton(self.frame_24)
        self.but_new_mission_steps.setObjectName(u"but_new_mission_steps")
        self.but_new_mission_steps.setGeometry(QRect(110, 10, 25, 24))
        self.but_new_mission_steps.setMaximumSize(QSize(16777215, 16777215))
        self.but_new_mission_steps.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(179, 179, 179);\n"
"	border: 2px solid rgb(179, 179, 179);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icons/16x16/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_new_mission_steps.setIcon(icon6)
        self.but_rmv_mission_block = QPushButton(self.frame_24)
        self.but_rmv_mission_block.setObjectName(u"but_rmv_mission_block")
        self.but_rmv_mission_block.setGeometry(QRect(140, 10, 25, 24))
        self.but_rmv_mission_block.setMaximumSize(QSize(16777215, 16777215))
        self.but_rmv_mission_block.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(179, 179, 179);\n"
"	border: 2px solid rgb(179, 179, 179);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icons/16x16/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_rmv_mission_block.setIcon(icon7)
        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(0, 50, 171, 371))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_26)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(12, 12, 52, 16))
        self.label_9 = QLabel(self.frame_26)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(71, 12, 23, 16))
        self.label_9.setMaximumSize(QSize(16777215, 20))
        self.dest_1 = QComboBox(self.frame_26)
        self.dest_1.setObjectName(u"dest_1")
        self.dest_1.setGeometry(QRect(12, 35, 52, 23))
        self.dest_1.setFont(font1)
        self.dest_1.setMouseTracking(False)
        self.dest_1.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.dest_1.setMaxVisibleItems(4)
        self.dest_1.setFrame(True)
        self.IBE_2 = QComboBox(self.frame_26)
        self.IBE_2.addItem("")
        self.IBE_2.addItem("")
        self.IBE_2.addItem("")
        self.IBE_2.setObjectName(u"IBE_2")
        self.IBE_2.setGeometry(QRect(71, 35, 95, 23))
        self.IBE_2.setFont(font1)
        self.IBE_2.setMouseTracking(False)
        self.IBE_2.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.IBE_2.setMaxVisibleItems(4)
        self.IBE_2.setFrame(True)
        self.dest_2 = QComboBox(self.frame_26)
        self.dest_2.setObjectName(u"dest_2")
        self.dest_2.setGeometry(QRect(12, 65, 52, 22))
        self.dest_2.setFont(font1)
        self.dest_2.setMouseTracking(False)
        self.dest_2.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.dest_2.setMaxVisibleItems(4)
        self.dest_2.setFrame(True)
        self.IBE_3 = QComboBox(self.frame_26)
        self.IBE_3.addItem("")
        self.IBE_3.addItem("")
        self.IBE_3.addItem("")
        self.IBE_3.setObjectName(u"IBE_3")
        self.IBE_3.setGeometry(QRect(71, 65, 95, 22))
        self.IBE_3.setFont(font1)
        self.IBE_3.setMouseTracking(False)
        self.IBE_3.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.IBE_3.setMaxVisibleItems(4)
        self.IBE_3.setFrame(True)
        self.dest_3 = QComboBox(self.frame_26)
        self.dest_3.setObjectName(u"dest_3")
        self.dest_3.setGeometry(QRect(12, 94, 52, 23))
        self.dest_3.setFont(font1)
        self.dest_3.setMouseTracking(False)
        self.dest_3.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.dest_3.setMaxVisibleItems(4)
        self.dest_3.setFrame(True)
        self.IBE_4 = QComboBox(self.frame_26)
        self.IBE_4.addItem("")
        self.IBE_4.addItem("")
        self.IBE_4.addItem("")
        self.IBE_4.setObjectName(u"IBE_4")
        self.IBE_4.setGeometry(QRect(71, 94, 95, 23))
        self.IBE_4.setFont(font1)
        self.IBE_4.setMouseTracking(False)
        self.IBE_4.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.IBE_4.setMaxVisibleItems(4)
        self.IBE_4.setFrame(True)
        self.dest_4 = QComboBox(self.frame_26)
        self.dest_4.setObjectName(u"dest_4")
        self.dest_4.setGeometry(QRect(12, 124, 52, 23))
        self.dest_4.setFont(font1)
        self.dest_4.setMouseTracking(False)
        self.dest_4.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.dest_4.setMaxVisibleItems(4)
        self.dest_4.setFrame(True)
        self.IBE_5 = QComboBox(self.frame_26)
        self.IBE_5.addItem("")
        self.IBE_5.addItem("")
        self.IBE_5.addItem("")
        self.IBE_5.setObjectName(u"IBE_5")
        self.IBE_5.setGeometry(QRect(71, 124, 95, 23))
        self.IBE_5.setFont(font1)
        self.IBE_5.setMouseTracking(False)
        self.IBE_5.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.IBE_5.setMaxVisibleItems(4)
        self.IBE_5.setFrame(True)
        self.dest_5 = QComboBox(self.frame_26)
        self.dest_5.setObjectName(u"dest_5")
        self.dest_5.setGeometry(QRect(12, 154, 52, 23))
        self.dest_5.setFont(font1)
        self.dest_5.setMouseTracking(False)
        self.dest_5.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.dest_5.setMaxVisibleItems(4)
        self.dest_5.setFrame(True)
        self.IBE_6 = QComboBox(self.frame_26)
        self.IBE_6.addItem("")
        self.IBE_6.addItem("")
        self.IBE_6.addItem("")
        self.IBE_6.setObjectName(u"IBE_6")
        self.IBE_6.setGeometry(QRect(71, 154, 95, 23))
        self.IBE_6.setFont(font1)
        self.IBE_6.setMouseTracking(False)
        self.IBE_6.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.IBE_6.setMaxVisibleItems(4)
        self.IBE_6.setFrame(True)
        self.dest_6 = QComboBox(self.frame_26)
        self.dest_6.setObjectName(u"dest_6")
        self.dest_6.setGeometry(QRect(12, 184, 52, 22))
        self.dest_6.setFont(font1)
        self.dest_6.setMouseTracking(False)
        self.dest_6.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.dest_6.setMaxVisibleItems(4)
        self.dest_6.setFrame(True)
        self.IBE_7 = QComboBox(self.frame_26)
        self.IBE_7.addItem("")
        self.IBE_7.addItem("")
        self.IBE_7.addItem("")
        self.IBE_7.setObjectName(u"IBE_7")
        self.IBE_7.setGeometry(QRect(71, 184, 95, 22))
        self.IBE_7.setFont(font1)
        self.IBE_7.setMouseTracking(False)
        self.IBE_7.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.IBE_7.setMaxVisibleItems(4)
        self.IBE_7.setFrame(True)
        self.dest_7 = QComboBox(self.frame_26)
        self.dest_7.setObjectName(u"dest_7")
        self.dest_7.setGeometry(QRect(12, 213, 52, 23))
        self.dest_7.setFont(font1)
        self.dest_7.setMouseTracking(False)
        self.dest_7.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.dest_7.setMaxVisibleItems(4)
        self.dest_7.setFrame(True)
        self.IBE_8 = QComboBox(self.frame_26)
        self.IBE_8.addItem("")
        self.IBE_8.addItem("")
        self.IBE_8.addItem("")
        self.IBE_8.setObjectName(u"IBE_8")
        self.IBE_8.setGeometry(QRect(71, 213, 95, 23))
        self.IBE_8.setFont(font1)
        self.IBE_8.setMouseTracking(False)
        self.IBE_8.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.IBE_8.setMaxVisibleItems(4)
        self.IBE_8.setFrame(True)
        self.dest_8 = QComboBox(self.frame_26)
        self.dest_8.setObjectName(u"dest_8")
        self.dest_8.setGeometry(QRect(12, 243, 52, 23))
        self.dest_8.setFont(font1)
        self.dest_8.setMouseTracking(False)
        self.dest_8.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.dest_8.setMaxVisibleItems(4)
        self.dest_8.setFrame(True)
        self.IBE_9 = QComboBox(self.frame_26)
        self.IBE_9.addItem("")
        self.IBE_9.addItem("")
        self.IBE_9.addItem("")
        self.IBE_9.setObjectName(u"IBE_9")
        self.IBE_9.setGeometry(QRect(71, 243, 95, 23))
        self.IBE_9.setFont(font1)
        self.IBE_9.setMouseTracking(False)
        self.IBE_9.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.IBE_9.setMaxVisibleItems(4)
        self.IBE_9.setFrame(True)
        self.dest_9 = QComboBox(self.frame_26)
        self.dest_9.setObjectName(u"dest_9")
        self.dest_9.setGeometry(QRect(12, 273, 52, 22))
        self.dest_9.setFont(font1)
        self.dest_9.setMouseTracking(False)
        self.dest_9.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.dest_9.setMaxVisibleItems(4)
        self.dest_9.setFrame(True)
        self.IBE_10 = QComboBox(self.frame_26)
        self.IBE_10.addItem("")
        self.IBE_10.addItem("")
        self.IBE_10.addItem("")
        self.IBE_10.setObjectName(u"IBE_10")
        self.IBE_10.setGeometry(QRect(71, 273, 95, 22))
        self.IBE_10.setFont(font1)
        self.IBE_10.setMouseTracking(False)
        self.IBE_10.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.IBE_10.setMaxVisibleItems(4)
        self.IBE_10.setFrame(True)
        self.dest_10 = QComboBox(self.frame_26)
        self.dest_10.setObjectName(u"dest_10")
        self.dest_10.setGeometry(QRect(12, 302, 52, 23))
        self.dest_10.setFont(font1)
        self.dest_10.setMouseTracking(False)
        self.dest_10.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.dest_10.setMaxVisibleItems(4)
        self.dest_10.setFrame(True)
        self.IBE_11 = QComboBox(self.frame_26)
        self.IBE_11.addItem("")
        self.IBE_11.addItem("")
        self.IBE_11.addItem("")
        self.IBE_11.setObjectName(u"IBE_11")
        self.IBE_11.setGeometry(QRect(71, 302, 95, 23))
        self.IBE_11.setFont(font1)
        self.IBE_11.setMouseTracking(False)
        self.IBE_11.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.IBE_11.setMaxVisibleItems(4)
        self.IBE_11.setFrame(True)
        self.dest_11 = QComboBox(self.frame_26)
        self.dest_11.setObjectName(u"dest_11")
        self.dest_11.setGeometry(QRect(12, 332, 52, 23))
        self.dest_11.setFont(font1)
        self.dest_11.setMouseTracking(False)
        self.dest_11.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.dest_11.setMaxVisibleItems(4)
        self.dest_11.setFrame(True)
        self.IBE_12 = QComboBox(self.frame_26)
        self.IBE_12.addItem("")
        self.IBE_12.addItem("")
        self.IBE_12.addItem("")
        self.IBE_12.setObjectName(u"IBE_12")
        self.IBE_12.setGeometry(QRect(71, 332, 95, 23))
        self.IBE_12.setFont(font1)
        self.IBE_12.setMouseTracking(False)
        self.IBE_12.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.IBE_12.setMaxVisibleItems(4)
        self.IBE_12.setFrame(True)

        self.verticalLayout_11.addWidget(self.frame_24)


        self.verticalLayout_10.addWidget(self.frame_22)

        self.new_mission_button_frame = QFrame(self.frame_10)
        self.new_mission_button_frame.setObjectName(u"new_mission_button_frame")
        self.new_mission_button_frame.setMinimumSize(QSize(0, 60))
        self.new_mission_button_frame.setMaximumSize(QSize(16777215, 80))
        self.new_mission_button_frame.setFrameShape(QFrame.StyledPanel)
        self.new_mission_button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.new_mission_button_frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.but_send_mission = QPushButton(self.new_mission_button_frame)
        self.but_send_mission.setObjectName(u"but_send_mission")
        self.but_send_mission.setMaximumSize(QSize(16777215, 16777215))
        self.but_send_mission.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: rgb(179, 179, 179);\n"
"	border: 2px solid rgb(179, 179, 179);\n"
"}")
        self.but_send_mission.setIcon(icon4)
        self.but_send_mission.setIconSize(QSize(20, 20))

        self.verticalLayout_12.addWidget(self.but_send_mission)

        self.but_cancel_new_mission = QPushButton(self.new_mission_button_frame)
        self.but_cancel_new_mission.setObjectName(u"but_cancel_new_mission")
        self.but_cancel_new_mission.setMaximumSize(QSize(16777215, 16777215))
        self.but_cancel_new_mission.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.but_cancel_new_mission.setIcon(icon8)

        self.verticalLayout_12.addWidget(self.but_cancel_new_mission)


        self.verticalLayout_10.addWidget(self.new_mission_button_frame)


        self.verticalLayout_9.addWidget(self.frame_10)


        self.verticalLayout_8.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.mission_page)

        self.verticalLayout_3.addWidget(self.stackedWidget)


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
        self.frame_13.setMaximumSize(QSize(16777215, 50))
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
        self.frame_12.setMinimumSize(QSize(0, 50))
        self.frame_12.setMaximumSize(QSize(16777215, 50))
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
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setWeight(50)
        self.title_log_5.setFont(font2)
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
        self.title_log_6.setFont(font2)
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
        self.title_log_7.setFont(font2)
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
        self.title_log_8.setFont(font2)
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
        self.title_log_9.setFont(font2)
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
        self.title_log_10.setFont(font2)
        self.title_log_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.title_log_10)


        self.verticalLayout_6.addWidget(self.frame_19)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_flags)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 120))
        self.frame_8.setMaximumSize(QSize(16777215, 150))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.layout_plot_battery = QVBoxLayout(self.frame_8)
        self.layout_plot_battery.setObjectName(u"layout_plot_battery")

        self.verticalLayout_5.addWidget(self.frame_8)


        self.horizontalLayout.addWidget(self.frame_flags)


        self.verticalLayout.addWidget(self.frame_info)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.IBE_1.setCurrentIndex(0)
        self.dest_1.setCurrentIndex(-1)
        self.IBE_2.setCurrentIndex(0)
        self.dest_2.setCurrentIndex(-1)
        self.IBE_3.setCurrentIndex(0)
        self.dest_3.setCurrentIndex(-1)
        self.IBE_4.setCurrentIndex(0)
        self.dest_4.setCurrentIndex(-1)
        self.IBE_5.setCurrentIndex(0)
        self.dest_5.setCurrentIndex(-1)
        self.IBE_6.setCurrentIndex(0)
        self.dest_6.setCurrentIndex(-1)
        self.IBE_7.setCurrentIndex(0)
        self.dest_7.setCurrentIndex(-1)
        self.IBE_8.setCurrentIndex(0)
        self.dest_8.setCurrentIndex(-1)
        self.IBE_9.setCurrentIndex(0)
        self.dest_9.setCurrentIndex(-1)
        self.IBE_10.setCurrentIndex(0)
        self.dest_10.setCurrentIndex(-1)
        self.IBE_11.setCurrentIndex(0)
        self.dest_11.setCurrentIndex(-1)
        self.IBE_12.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.icon_log.setText("")
        self.title_log.setText(QCoreApplication.translate("MainWindow", u"Log", None))
        self.but_back_to_missions.setText("")
        self.icon_log_5.setText("")
        self.title_log_11.setText(QCoreApplication.translate("MainWindow", u"Houston actions", None))
        self.but_select_log.setText("")
        self.but_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.but_pause_or_continue.setText(QCoreApplication.translate("MainWindow", u"Pause mission", None))
        self.but_new_mission.setText(QCoreApplication.translate("MainWindow", u"Start new mission", None))
        self.but_abort_mission.setText(QCoreApplication.translate("MainWindow", u"Abort mission", None))
        self.icon_log_6.setText("")
        self.title_log_12.setText(QCoreApplication.translate("MainWindow", u"New mission", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Initial IBE", None))
        self.IBE_1.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.IBE_1.setItemText(1, QCoreApplication.translate("MainWindow", u"Button", None))
        self.IBE_1.setItemText(2, QCoreApplication.translate("MainWindow", u"Houston", None))

        self.IBE_1.setCurrentText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Blocks", None))
        self.but_new_mission_steps.setText("")
        self.but_rmv_mission_block.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"To node:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"IBE:", None))
        self.dest_1.setCurrentText("")
        self.IBE_2.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.IBE_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Button", None))
        self.IBE_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Houston", None))

        self.IBE_2.setCurrentText(QCoreApplication.translate("MainWindow", u"None", None))
        self.dest_2.setCurrentText("")
        self.IBE_3.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.IBE_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Button", None))
        self.IBE_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Houston", None))

        self.IBE_3.setCurrentText(QCoreApplication.translate("MainWindow", u"None", None))
        self.dest_3.setCurrentText("")
        self.IBE_4.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.IBE_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Button", None))
        self.IBE_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Houston", None))

        self.IBE_4.setCurrentText(QCoreApplication.translate("MainWindow", u"None", None))
        self.dest_4.setCurrentText("")
        self.IBE_5.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.IBE_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Button", None))
        self.IBE_5.setItemText(2, QCoreApplication.translate("MainWindow", u"Houston", None))

        self.IBE_5.setCurrentText(QCoreApplication.translate("MainWindow", u"None", None))
        self.dest_5.setCurrentText("")
        self.IBE_6.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.IBE_6.setItemText(1, QCoreApplication.translate("MainWindow", u"Button", None))
        self.IBE_6.setItemText(2, QCoreApplication.translate("MainWindow", u"Houston", None))

        self.IBE_6.setCurrentText(QCoreApplication.translate("MainWindow", u"None", None))
        self.dest_6.setCurrentText("")
        self.IBE_7.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.IBE_7.setItemText(1, QCoreApplication.translate("MainWindow", u"Button", None))
        self.IBE_7.setItemText(2, QCoreApplication.translate("MainWindow", u"Houston", None))

        self.IBE_7.setCurrentText(QCoreApplication.translate("MainWindow", u"None", None))
        self.dest_7.setCurrentText("")
        self.IBE_8.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.IBE_8.setItemText(1, QCoreApplication.translate("MainWindow", u"Button", None))
        self.IBE_8.setItemText(2, QCoreApplication.translate("MainWindow", u"Houston", None))

        self.IBE_8.setCurrentText(QCoreApplication.translate("MainWindow", u"None", None))
        self.dest_8.setCurrentText("")
        self.IBE_9.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.IBE_9.setItemText(1, QCoreApplication.translate("MainWindow", u"Button", None))
        self.IBE_9.setItemText(2, QCoreApplication.translate("MainWindow", u"Houston", None))

        self.IBE_9.setCurrentText(QCoreApplication.translate("MainWindow", u"None", None))
        self.dest_9.setCurrentText("")
        self.IBE_10.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.IBE_10.setItemText(1, QCoreApplication.translate("MainWindow", u"Button", None))
        self.IBE_10.setItemText(2, QCoreApplication.translate("MainWindow", u"Houston", None))

        self.IBE_10.setCurrentText(QCoreApplication.translate("MainWindow", u"None", None))
        self.dest_10.setCurrentText("")
        self.IBE_11.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.IBE_11.setItemText(1, QCoreApplication.translate("MainWindow", u"Button", None))
        self.IBE_11.setItemText(2, QCoreApplication.translate("MainWindow", u"Houston", None))

        self.IBE_11.setCurrentText(QCoreApplication.translate("MainWindow", u"None", None))
        self.dest_11.setCurrentText("")
        self.IBE_12.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.IBE_12.setItemText(1, QCoreApplication.translate("MainWindow", u"Button", None))
        self.IBE_12.setItemText(2, QCoreApplication.translate("MainWindow", u"Houston", None))

        self.IBE_12.setCurrentText(QCoreApplication.translate("MainWindow", u"None", None))
        self.but_send_mission.setText(QCoreApplication.translate("MainWindow", u"Send Mission", None))
        self.but_cancel_new_mission.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
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
    # retranslateUi

