# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EcsLogChecker_Clt.ui'
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
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1750, 897)
        MainWindow.setMinimumSize(QSize(1000, 800))
        MainWindow.setMaximumSize(QSize(1750, 900))
        MainWindow.setContextMenuPolicy(Qt.ActionsContextMenu)
        MainWindow.setStyleSheet(u"")
        MainWindow.setDockNestingEnabled(False)
        self.actionhi = QAction(MainWindow)
        self.actionhi.setObjectName(u"actionhi")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 40, 300, 171))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textEditFind = QTextEdit(self.groupBox)
        self.textEditFind.setObjectName(u"textEditFind")
        self.textEditFind.setMaximumSize(QSize(300, 25))
        self.textEditFind.setLineWidth(50)

        self.gridLayout.addWidget(self.textEditFind, 0, 0, 1, 3)

        self.labelSearchNo = QLabel(self.groupBox)
        self.labelSearchNo.setObjectName(u"labelSearchNo")
        self.labelSearchNo.setMinimumSize(QSize(40, 0))
        self.labelSearchNo.setMaximumSize(QSize(45, 16777215))
        self.labelSearchNo.setStyleSheet(u"")

        self.gridLayout.addWidget(self.labelSearchNo, 1, 0, 1, 1)

        self.LCurrNo = QLabel(self.groupBox)
        self.LCurrNo.setObjectName(u"LCurrNo")
        self.LCurrNo.setMinimumSize(QSize(40, 0))
        self.LCurrNo.setMaximumSize(QSize(65, 16777215))
        self.LCurrNo.setStyleSheet(u"")

        self.gridLayout.addWidget(self.LCurrNo, 1, 1, 1, 1)

        self.BtnFind = QPushButton(self.groupBox)
        self.BtnFind.setObjectName(u"BtnFind")
        self.BtnFind.setMinimumSize(QSize(100, 0))
        self.BtnFind.setMaximumSize(QSize(100, 25))
        self.BtnFind.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.BtnFind, 1, 2, 1, 1)

        self.labelCurrNo = QLabel(self.groupBox)
        self.labelCurrNo.setObjectName(u"labelCurrNo")
        self.labelCurrNo.setMinimumSize(QSize(60, 0))
        self.labelCurrNo.setMaximumSize(QSize(25, 16777215))
        self.labelCurrNo.setStyleSheet(u"")

        self.gridLayout.addWidget(self.labelCurrNo, 2, 0, 1, 1)

        self.LSearchNo = QLabel(self.groupBox)
        self.LSearchNo.setObjectName(u"LSearchNo")
        self.LSearchNo.setMinimumSize(QSize(40, 0))
        self.LSearchNo.setMaximumSize(QSize(65, 16777215))
        self.LSearchNo.setStyleSheet(u"")

        self.gridLayout.addWidget(self.LSearchNo, 2, 1, 1, 1)

        self.BtnCurrRowSel = QPushButton(self.groupBox)
        self.BtnCurrRowSel.setObjectName(u"BtnCurrRowSel")
        self.BtnCurrRowSel.setEnabled(False)
        self.BtnCurrRowSel.setMinimumSize(QSize(100, 25))
        self.BtnCurrRowSel.setMaximumSize(QSize(100, 25))
        self.BtnCurrRowSel.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.BtnCurrRowSel, 2, 2, 1, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.comboBox, 3, 0, 1, 3)

        self.labelSearchNo_2 = QLabel(self.groupBox)
        self.labelSearchNo_2.setObjectName(u"labelSearchNo_2")
        self.labelSearchNo_2.setMinimumSize(QSize(40, 0))
        self.labelSearchNo_2.setMaximumSize(QSize(100, 16777215))
        self.labelSearchNo_2.setStyleSheet(u"")

        self.gridLayout.addWidget(self.labelSearchNo_2, 4, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 4, 2, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 0, 1721, 41))
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Btn_MesLog = QPushButton(self.groupBox_2)
        self.Btn_MesLog.setObjectName(u"Btn_MesLog")

        self.horizontalLayout.addWidget(self.Btn_MesLog)

        self.Btn_CnvLog = QPushButton(self.groupBox_2)
        self.Btn_CnvLog.setObjectName(u"Btn_CnvLog")

        self.horizontalLayout.addWidget(self.Btn_CnvLog)

        self.Btn_BcrLog = QPushButton(self.groupBox_2)
        self.Btn_BcrLog.setObjectName(u"Btn_BcrLog")

        self.horizontalLayout.addWidget(self.Btn_BcrLog)

        self.Btn_BcrNoReadLog = QPushButton(self.groupBox_2)
        self.Btn_BcrNoReadLog.setObjectName(u"Btn_BcrNoReadLog")

        self.horizontalLayout.addWidget(self.Btn_BcrNoReadLog)

        self.Btn_StcLog = QPushButton(self.groupBox_2)
        self.Btn_StcLog.setObjectName(u"Btn_StcLog")

        self.horizontalLayout.addWidget(self.Btn_StcLog)

        self.Btn_JobLog = QPushButton(self.groupBox_2)
        self.Btn_JobLog.setObjectName(u"Btn_JobLog")

        self.horizontalLayout.addWidget(self.Btn_JobLog)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(310, 40, 1420, 800))
        self.groupBox_3.setMinimumSize(QSize(0, 800))
        self.groupBox_3.setMaximumSize(QSize(16777215, 800))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableWidget = QTableWidget(self.groupBox_3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(1400, 750))
        self.tableWidget.setMaximumSize(QSize(1600, 750))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setFocusPolicy(Qt.ClickFocus)
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	border-radius:0px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSortingEnabled(True)

        self.horizontalLayout_2.addWidget(self.tableWidget)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 380, 300, 461))
        self.verticalLayout = QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(self.groupBox_4)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(280, 300))
        self.listWidget.setMaximumSize(QSize(300, 900))
        self.listWidget.setStyleSheet(u"QListWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
"}")

        self.verticalLayout.addWidget(self.listWidget)

        self.labelDownload = QLabel(self.groupBox_4)
        self.labelDownload.setObjectName(u"labelDownload")
        self.labelDownload.setMinimumSize(QSize(280, 0))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.labelDownload.setFont(font1)
        self.labelDownload.setStyleSheet(u"color: rgb(182, 10, 255);")
        self.labelDownload.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.labelDownload)

        self.progressBar = QProgressBar(self.groupBox_4)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setMinimumSize(QSize(280, 0))
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style:none;\n"
"	border-radius: 10px;\n"
"	text-align:center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.506, stop:0 rgba(170, 0, 255, 255), stop:1 rgba(188, 27, 199, 255));\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout.addWidget(self.progressBar)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 210, 301, 81))
        self.lineEdit = QLineEdit(self.groupBox_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(69, 14, 131, 21))
        self.pushButton = QPushButton(self.groupBox_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 13, 75, 23))
        self.label = QLabel(self.groupBox_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(11, 20, 56, 12))
        self.pushButton_2 = QPushButton(self.groupBox_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QRect(210, 43, 75, 23))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 38, 89);\n"
"color: rgb(75, 75, 75);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1750, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ECSLOGCHK", None))
        self.actionhi.setText(QCoreApplication.translate("MainWindow", u"hi", None))
        self.groupBox.setTitle("")
        self.labelSearchNo.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9 \uc218", None))
        self.LCurrNo.setText("")
        self.BtnFind.setText(QCoreApplication.translate("MainWindow", u"\ucc3e\uae30", None))
        self.labelCurrNo.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac \ubc88\ud638", None))
        self.LSearchNo.setText("")
        self.BtnCurrRowSel.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac \uc5f4 \uc120\ud0dd", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\uba54\uc138\uc9c0 ID \ub9ac\uc2a4\ud2b8", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CONVEYOR_EVENT", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CONVEYOR_REPLY", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"SEND_EVENT", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"SEND_REPLY", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"TRANSFER_IN_ECS_EVENT", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"TRANSFER_IN_ECS_REPLY", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"TRANSFER_OUT_ECS_EVENT", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"TRANSFER_OUT_ECS_REPLY", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"ALARM_EVENT", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"DATE_EVENT", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"DATE_REPLY", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"TRAY_EVENT", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"TRAYID_MATCHING_EVENT", None))

        self.labelSearchNo_2.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8 \ubc94\uc704 \uc124\uc815", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"10%", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"20%", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"30%", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"40%", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"50%", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"60%", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"70%", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"80%", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"90%", None))
        self.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"100%", None))

        self.groupBox_2.setTitle("")
        self.Btn_MesLog.setText(QCoreApplication.translate("MainWindow", u"MES", None))
        self.Btn_CnvLog.setText(QCoreApplication.translate("MainWindow", u"CNV", None))
        self.Btn_BcrLog.setText(QCoreApplication.translate("MainWindow", u"BCR", None))
        self.Btn_BcrNoReadLog.setText(QCoreApplication.translate("MainWindow", u"BCR NOREAD", None))
        self.Btn_StcLog.setText(QCoreApplication.translate("MainWindow", u"STC", None))
        self.Btn_JobLog.setText(QCoreApplication.translate("MainWindow", u"JOB", None))
        self.groupBox_3.setTitle("")
        self.groupBox_4.setTitle("")
        self.labelDownload.setText("")
        self.groupBox_5.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\uc11c\ubc84 \uc5f0\uacb0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc11c\ubc84  IP", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
    # retranslateUi

