from PyQt4 import QtCore, QtGui
import Ui_ModuleListWidget

class ModuleListWidgetItem(QtGui.QListWidgetItem):
	def __init__(self, parent=None):
		QtGui.QListWidgetItem.__init__(self, parent, 10000)
		self.ui = Ui_ModuleListWidget.Ui_ModuleListWidget()
		self.ui.setupUi(self)
