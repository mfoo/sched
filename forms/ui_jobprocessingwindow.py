# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jobprocessingwindow.ui'
#
# Created: Tue Mar 30 21:22:45 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(448, 440)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 400, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 21))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.label_2.setObjectName("label_2")
        self.startTimeLabel = QtGui.QLabel(Dialog)
        self.startTimeLabel.setGeometry(QtCore.QRect(220, 30, 221, 21))
        self.startTimeLabel.setObjectName("startTimeLabel")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 101, 16))
        self.label_4.setObjectName("label_4")
        self.durationLabel = QtGui.QLabel(Dialog)
        self.durationLabel.setGeometry(QtCore.QRect(220, 50, 221, 16))
        self.durationLabel.setObjectName("durationLabel")
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.label_6.setObjectName("label_6")
        self.completedLabel = QtGui.QLabel(Dialog)
        self.completedLabel.setGeometry(QtCore.QRect(220, 70, 221, 16))
        self.completedLabel.setObjectName("completedLabel")
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 90, 91, 16))
        self.label_8.setObjectName("label_8")
        self.remainingLabel = QtGui.QLabel(Dialog)
        self.remainingLabel.setGeometry(QtCore.QRect(220, 90, 221, 16))
        self.remainingLabel.setObjectName("remainingLabel")
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 120, 431, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_18 = QtGui.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(10, 150, 52, 15))
        self.label_18.setObjectName("label_18")
        self.logText = QtGui.QPlainTextEdit(Dialog)
        self.logText.setGeometry(QtCore.QRect(10, 170, 431, 221))
        self.logText.setReadOnly(True)
        self.logText.setCenterOnScroll(True)
        self.logText.setObjectName("logText")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Processing", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Sched is currently running tasks.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Job start time:", None, QtGui.QApplication.UnicodeUTF8))
        self.startTimeLabel.setText(QtGui.QApplication.translate("Dialog", "5pm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Current duration:", None, QtGui.QApplication.UnicodeUTF8))
        self.durationLabel.setText(QtGui.QApplication.translate("Dialog", "1 hour", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Jobs completed:", None, QtGui.QApplication.UnicodeUTF8))
        self.completedLabel.setText(QtGui.QApplication.translate("Dialog", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Jobs remaining:", None, QtGui.QApplication.UnicodeUTF8))
        self.remainingLabel.setText(QtGui.QApplication.translate("Dialog", "150", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Dialog", "Output:", None, QtGui.QApplication.UnicodeUTF8))

