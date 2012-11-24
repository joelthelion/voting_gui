# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results.ui'
#
# Created: Sat Nov 24 15:19:45 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_results(object):
    def setupUi(self, results):
        results.setObjectName(_fromUtf8("results"))
        results.resize(471, 411)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        results.setWindowIcon(icon)
        results.setStyleSheet(_fromUtf8("QDialog#results {\n"
"    background-image: url(:/all/nounours_cropped.png); }"))
        self.verticalLayout = QtGui.QVBoxLayout(results)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.table = QtGui.QTableWidget(results)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table.setColumnCount(3)
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.table)
        self.buttonBox = QtGui.QDialogButtonBox(results)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(results)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), results.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), results.reject)
        QtCore.QMetaObject.connectSlotsByName(results)

    def retranslateUi(self, results):
        results.setWindowTitle(QtGui.QApplication.translate("results", "Résultats!", None, QtGui.QApplication.UnicodeUTF8))
        self.table.setSortingEnabled(True)
        item = self.table.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("results", "Rang", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("results", "Prénom", None, QtGui.QApplication.UnicodeUTF8))
        item = self.table.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("results", "Résultat", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
