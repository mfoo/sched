# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newmodulewizard.ui'
#
# Created: Mon Mar 29 18:22:02 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(399, 354)
        self.okCancelButtons = QtGui.QDialogButtonBox(Dialog)
        self.okCancelButtons.setGeometry(QtCore.QRect(50, 290, 341, 32))
        self.okCancelButtons.setOrientation(QtCore.Qt.Horizontal)
        self.okCancelButtons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.okCancelButtons.setObjectName("okCancelButtons")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 351, 16))
        self.label.setObjectName("label")
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 71, 16))
        self.label_5.setObjectName("label_5")
        self.globalScopeRadioButton = QtGui.QRadioButton(Dialog)
        self.globalScopeRadioButton.setGeometry(QtCore.QRect(190, 260, 93, 20))
        self.globalScopeRadioButton.setObjectName("globalScopeRadioButton")
        self.newParameterButton = QtGui.QPushButton(Dialog)
        self.newParameterButton.setGeometry(QtCore.QRect(310, 150, 81, 27))
        self.newParameterButton.setObjectName("newParameterButton")
        self.projectScopeRadioButton = QtGui.QRadioButton(Dialog)
        self.projectScopeRadioButton.setGeometry(QtCore.QRect(90, 260, 93, 20))
        self.projectScopeRadioButton.setObjectName("projectScopeRadioButton")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 52, 15))
        self.label_3.setObjectName("label_3")
        self.removeParameterButton = QtGui.QPushButton(Dialog)
        self.removeParameterButton.setGeometry(QtCore.QRect(310, 180, 81, 27))
        self.removeParameterButton.setObjectName("removeParameterButton")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 250, 71, 31))
        self.label_2.setObjectName("label_2")
        self.nameInputBox = QtGui.QLineEdit(Dialog)
        self.nameInputBox.setGeometry(QtCore.QRect(90, 40, 301, 23))
        self.nameInputBox.setObjectName("nameInputBox")
        self.parameterList = QtGui.QTableWidget(Dialog)
        self.parameterList.setGeometry(QtCore.QRect(10, 150, 291, 91))
        self.parameterList.setColumnCount(3)
        self.parameterList.setObjectName("parameterList")
        self.parameterList.setColumnCount(3)
        self.parameterList.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.parameterList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.parameterList.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.parameterList.setHorizontalHeaderItem(2, item)
        self.parameterList.verticalHeader().setVisible(False)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_4.setObjectName("label_4")
        self.commandInputBox = QtGui.QLineEdit(Dialog)
        self.commandInputBox.setGeometry(QtCore.QRect(90, 70, 301, 23))
        self.commandInputBox.setObjectName("commandInputBox")
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_6.setObjectName("label_6")
        self.descriptionInputBox = QtGui.QLineEdit(Dialog)
        self.descriptionInputBox.setGeometry(QtCore.QRect(90, 100, 301, 23))
        self.descriptionInputBox.setObjectName("descriptionInputBox")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.okCancelButtons, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.okCancelButtons, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Add New Module", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Use this wizard to add a new module to Sched.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Parameters:", None, QtGui.QApplication.UnicodeUTF8))
        self.globalScopeRadioButton.setText(QtGui.QApplication.translate("Dialog", "All Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.newParameterButton.setText(QtGui.QApplication.translate("Dialog", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.projectScopeRadioButton.setText(QtGui.QApplication.translate("Dialog", "This Project", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.removeParameterButton.setText(QtGui.QApplication.translate("Dialog", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Available to:", None, QtGui.QApplication.UnicodeUTF8))
        self.parameterList.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Dialog", "Symbol", None, QtGui.QApplication.UnicodeUTF8))
        self.parameterList.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Dialog", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.parameterList.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Dialog", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Command:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Description:", None, QtGui.QApplication.UnicodeUTF8))

