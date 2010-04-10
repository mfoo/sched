# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Fri Apr  9 20:36:24 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(140, 40, 401, 181))
        self.treeWidget.setAcceptDrops(True)
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.treeWidget.addTopLevelItem(QtGui.QTreeWidgetItem(["lol"]))

    ui.treeWidget.addTopLevelItem(QtGui.QTreeWidgetItem(["lott"]))
    ui.treeWidget.itemAt(0,0).addChild(QtGui.QTreeWidgetItem(["ahah"]))
    MainWindow.show()
    sys.exit(app.exec_())

