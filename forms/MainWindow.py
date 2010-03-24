#from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from forms.Ui_MainWindow import Ui_MainWindow
from imports import Module, Parameter
from forms.Ui_ModuleListWidget import Ui_ModuleListWidget

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.connect(self.ui.listWidget, SIGNAL("itemClicked(QListWidgetItem*)"), self.globalModuleListClickHandler)
		self.connect(self.ui.projectModuleList, SIGNAL("itemClicked(QListWidgetItem*)"), self.projectModuleListClickHandler)

		headers = ["Symbol", "Description", "Mapping"]
		self.ui.mappingsTable.setColumnCount(len(headers))
		self.ui.mappingsTable.setHorizontalHeaderLabels(headers)

	def globalModuleListClickHandler(self, item):
		self.ui.projectModuleList.addItem(Ui_ModuleListWidget(item.module))

	def projectModuleListClickHandler(self, item):
		"""
		When a module is clicked on in the current project list,
		populate the command line box with it's command.
		"""
		self.ui.commandEdit.setText(QString(item.module.command))

