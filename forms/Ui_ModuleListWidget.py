# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/modulelistwidget.ui'
#
# Created: Mon Mar 22 22:12:03 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from imports import Module, Parameter

class Ui_ModuleListWidget(QtGui.QListWidgetItem):
    def __init__(self, module, parent = None):
    	self.module = module
        super(Ui_ModuleListWidget, self).__init__(parent)
#        self.resize(239, 72)
#        self.pushButton = QtGui.QPushButton()
	
#	vbox = QtGui.QVBoxLayout()
#        vbox.addStretch(1)
#        self.setGeometry(00,0,20,20)
#        self.setLayout(vbox)
        labelText=QtCore.QString()	
        self.label = QtGui.QLabel(labelText)
        self.lineEdit = QtGui.QLineEdit()
#	position = QtGui.LEFT
#        self.label.setBuddy(self.lineEdit)
        layout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight)
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        #self.setLayout(layout)
        self.setText(QtCore.QString(self.module.name))



#    def setupUi(self, ModuleListWidget):
       # ModuleListWidget.setObjectName("ModuleListWidget")
#        ModuleListWidget.resize(239, 72)
#        self.pushButton = QtGui.QPushButton(ModuleListWidget)
#        self.pushButton.setGeometry(QtCore.QRect(80, 20, 85, 27))
#        self.pushButton.setObjectName("pushButton")

#        self.retranslateUi(ModuleListWidget)
#        QtCore.QMetaObject.connectSlotsByName(ModuleListWidget)

#    def retranslateUi(self, ModuleListWidget):
#        ModuleListWidget.setWindowTitle(QtGui.QApplication.translate("ModuleListWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
#        self.pushButton.setText(QtGui.QApplication.translate("ModuleListWidget", "PushButton", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ModuleListWidget = QtGui.QWidget()
    ui = Ui_ModuleListWidget()
    ui.setupUi(ModuleListWidget)
    ModuleListWidget.show()
    sys.exit(app.exec_())

