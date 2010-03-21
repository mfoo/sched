# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modulelistwidget.ui'
#
# Created: Sun Mar 21 17:02:30 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ModuleListWidget(object):
    def setupUi(self, ModuleListWidget):
        ModuleListWidget.setObjectName("ModuleListWidget")
        ModuleListWidget.resize(239, 72)
        self.pushButton = QtGui.QPushButton(ModuleListWidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 20, 85, 27))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(ModuleListWidget)
        QtCore.QMetaObject.connectSlotsByName(ModuleListWidget)

    def retranslateUi(self, ModuleListWidget):
        ModuleListWidget.setWindowTitle(QtGui.QApplication.translate("ModuleListWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ModuleListWidget", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

