# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prenom.ui'
#
# Created: Sun Nov 28 13:07:50 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(335, 264)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("QWidget#centralwidget {background-image: url(:/all/nounours_cropped.png);}"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.prenom1 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.prenom1.setFont(font)
        self.prenom1.setText(_fromUtf8(""))
        self.prenom1.setAlignment(QtCore.Qt.AlignCenter)
        self.prenom1.setObjectName(_fromUtf8("prenom1"))
        self.horizontalLayout_2.addWidget(self.prenom1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.prenom2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.prenom2.setFont(font)
        self.prenom2.setAutoFillBackground(False)
        self.prenom2.setText(_fromUtf8(""))
        self.prenom2.setAlignment(QtCore.Qt.AlignCenter)
        self.prenom2.setObjectName(_fromUtf8("prenom2"))
        self.horizontalLayout_2.addWidget(self.prenom2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.button1 = QtGui.QPushButton(self.centralwidget)
        self.button1.setObjectName(_fromUtf8("button1"))
        self.horizontalLayout.addWidget(self.button1)
        self.button_equal = QtGui.QPushButton(self.centralwidget)
        self.button_equal.setObjectName(_fromUtf8("button_equal"))
        self.horizontalLayout.addWidget(self.button_equal)
        self.button2 = QtGui.QPushButton(self.centralwidget)
        self.button2.setObjectName(_fromUtf8("button2"))
        self.horizontalLayout.addWidget(self.button2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 335, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionResults = QtGui.QAction(MainWindow)
        self.actionResults.setObjectName(_fromUtf8("actionResults"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionResults)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Super Prénom!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "ou", None, QtGui.QApplication.UnicodeUTF8))
        self.button1.setText(QtGui.QApplication.translate("MainWindow", "Oui!", None, QtGui.QApplication.UnicodeUTF8))
        self.button_equal.setText(QtGui.QApplication.translate("MainWindow", "C\'est égal", None, QtGui.QApplication.UnicodeUTF8))
        self.button2.setText(QtGui.QApplication.translate("MainWindow", "Oui!", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "Fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.actionResults.setText(QtGui.QApplication.translate("MainWindow", "Voir résultats", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quitter", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
