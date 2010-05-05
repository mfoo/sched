# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treeview.ui'
#
# Created: Fri Apr  9 15:10:14 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class myview(QtGui.QTreeView):
   def __init__(self, parent=None):
        QtGui.QTreeView.__init__(self, parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
#        self.view.setDragDropMode(QtGui.QAbstractItemView.InternalMove)      
        self.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
#        model.setSupportedDragActions(QtCore.Qt.MoveAction)

   def dropIndicatorPosition(self):
       return QtGui.QAbstractItemView.AboveItem | QtGui.QAbstractItemView.BelowItem

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(573, 468)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.view = myview(self.centralwidget)
        self.view.setAlternatingRowColors(True)
        self.view.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.view.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.view.setTextElideMode(QtCore.Qt.ElideRight)
        self.view.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.view.setAnimated(False)
        self.view.setObjectName("view")
        self.vboxlayout.addWidget(self.view)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Editable Tree Model", None, QtGui.QApplication.UnicodeUTF8))
