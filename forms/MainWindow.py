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
		
		# Configure individual column widths
		self.ui.mappingsTable.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)
		self.ui.mappingsTable.horizontalHeader().setResizeMode(1, QHeaderView.Stretch)
		self.ui.mappingsTable.horizontalHeader().setResizeMode(2, QHeaderView.ResizeToContents)
		
		self.connect(self.ui.listWidget, SIGNAL("itemClicked(QListWidgetItem*)"), self.globalModuleListClickHandler)
		self.connect(self.ui.projectModuleList, SIGNAL("itemClicked(QListWidgetItem*)"), self.projectModuleListClickHandler)

		headers = ["Symbol", "Description", "Mapping"]
		self.ui.mappingsTable.setColumnCount(len(headers))
		self.ui.mappingsTable.setHorizontalHeaderLabels(headers)

		self.connect(self.ui.newGlobalModuleButton, SIGNAL("clicked()"), self.globalModuleButtonClicked)

		self.connect(self.ui.newProjectModuleButton, SIGNAL("clicked()"), self.projectModuleButtonClicked)

	def globalModuleButtonClicked(self):
		"""
		Shows a 'New Module' wizard that creates a global module (all projects)
		"""
		self.showNewModuleWizard(False)


	def projectModuleButtonClicked(self):
		"""
		Shows a 'New Module' wizard that creates a local module (this project only)
		"""
		self.showNewModuleWizard(True)
	

	def showNewModuleWizard(self, type):
		from forms.NewModuleWizard import NewModuleWizard
		self.newModuleWizard = NewModuleWizard(parent = self, local = type, callback = self.addNewModule)
		self.newModuleWizard.show()

	def addNewModule(self, module, local):
		print module.command
		print module.name
		print module.description
		for param in module.parameters:
			print param.id
			print param.description
			print param.value
		self.ui.listWidget.addItem(Ui_ModuleListWidget(module))
		self.updateMappings()

	def updateMappings(self):
		dataType = QMimeData()
		modules = [self.ui.projectModuleList.item(x).module for x in xrange(0, self.ui.projectModuleList.count())]
		self.ui.mappingsTable.setSortingEnabled(False)
		self.ui.mappingsTable.setRowCount(sum([len(x.parameters) for x in modules]) +1)

		counter = 0
		for module in modules:
			for param in module.parameters:
				self.ui.mappingsTable.setItem(counter, 0, QTableWidgetItem(QString(param.id)))
				self.ui.mappingsTable.setItem(counter, 1, QTableWidgetItem(QString(param.description)))
				self.ui.mappingsTable.setItem(counter, 2, QTableWidgetItem(QString(param.value)))
				counter += 1

		self.ui.mappingsTable.setSortingEnabled(True)
		
	
	def globalModuleListClickHandler(self, item):
		self.ui.projectModuleList.addItem(Ui_ModuleListWidget(item.module))
		self.updateMappings()

	def projectModuleListClickHandler(self, item):
		"""
		When a module is clicked on in the current project list,
		populate the command line box with it's command.
		"""
		self.ui.commandEdit.setText(QString(item.module.command))

