# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jobprocessingwindow.ui'
#
# Created: Mon Mar 29 18:22:02 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(448, 500)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 460, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 21))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(220, 30, 52, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(220, 50, 52, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(220, 70, 52, 15))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 90, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(220, 90, 52, 15))
        self.label_9.setObjectName("label_9")
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 120, 431, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(10, 180, 431, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(10, 220, 431, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(10, 300, 431, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(10, 260, 431, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(10, 200, 71, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(10, 280, 71, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtGui.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(10, 240, 71, 16))
        self.label_17.setObjectName("label_17")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Processing", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Sched is currently running tasks.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Job start time:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "5pm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Current duration:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "1 hour", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Jobs completed:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Jobs remaining:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "150", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "Core 1 Task:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "enfuse -o out.tiff *.jpg", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Dialog", "enfuse -o out.tiff *.jpg", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Dialog", "enfuse -o out.tiff *.jpg", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Dialog", "enfuse -o out.tiff *.jpg", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Dialog", "Core 2 Task:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Dialog", "Core 4 Task:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Dialog", "Core 3 Task:", None, QtGui.QApplication.UnicodeUTF8))

