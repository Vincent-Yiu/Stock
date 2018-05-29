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
        self.pushButton_select_T.setGeometry(QtCore.QRect(160, 70, 80, 23))
        self.pushButton_select_T.setObjectName("pushButton_select_T")
        self.pushButton_save_all = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_all.setGeometry(QtCore.QRect(60, 70, 41, 21))
        self.pushButton_save_all.setObjectName("pushButton_save_all")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 70, 41, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_save_percent = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_percent.setGeometry(QtCore.QRect(110, 70, 41, 21))
        self.pushButton_save_percent.setObjectName("pushButton_save_percent")
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
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        self.label_1.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_select_T.setText(_translate("MainWindow", "select_T"))
        self.pushButton_save_all.setText(_translate("MainWindow", "saveA"))
        self.pushButton_save_percent.setText(_translate("MainWindow", "saveP"))

