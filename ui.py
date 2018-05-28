# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(269, 161)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(0, 0, 181, 61))
        self.label_1.setObjectName("label_1")
        self.pushButton_select_T = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_select_T.setGeometry(QtCore.QRect(90, 70, 80, 23))
        self.pushButton_select_T.setObjectName("pushButton_select_T")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(0, 70, 81, 21))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_top = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_top.setGeometry(QtCore.QRect(180, 70, 41, 21))
        self.pushButton_top.setObjectName("pushButton_top")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 269, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_select_T.setText(_translate("MainWindow", "select_T"))
        self.pushButton_save.setText(_translate("MainWindow", "save"))
        self.pushButton_top.setText(_translate("MainWindow", "top"))

