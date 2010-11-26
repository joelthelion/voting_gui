# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results.ui'
#
# Created by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_results(object):
    def setupUi(self, results):
        results.setObjectName("results")
        results.resize(290, 411)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/all/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        results.setWindowIcon(icon)
        results.setStyleSheet("QDialog#results {\n"
"    background-image: url(:/all/nounours_cropped.png); }")
        self.verticalLayout = QtGui.QVBoxLayout(results)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtGui.QTableWidget(results)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table.setColumnCount(2)
        self.table.setObjectName("table")
        self.table.setColumnCount(2)
        self.table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.table)
        self.buttonBox = QtGui.QDialogButtonBox(results)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(results)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), results.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), results.reject)
        QtCore.QMetaObject.connectSlotsByName(results)

    def retranslateUi(self, results):
        results.setWindowTitle(QtGui.QApplication.translate("results", "Résultats!", None, QtGui.QApplication.UnicodeUTF8))
        self.table.setSortingEnabled(True)
        self.table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("results", "Prénom", None, QtGui.QApplication.UnicodeUTF8))
        self.table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("results", "Résultat", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
