from PyQt4.QtGui import *
from PyQt4.QtCore import *
from forms.Ui_NewModuleWizard import Ui_Dialog
from imports.Module import Module
from imports.Parameter import Parameter

class NewModuleWizard(QDialog):
	def __init__(self, parent=None, local = True, callback = True):
		QDialog.__init__(self, parent)

		self.callback = callback
		self.local = local
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		self.ui.parameterList.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)
		self.ui.parameterList.horizontalHeader().setResizeMode(1, QHeaderView.Stretch)
		self.ui.parameterList.horizontalHeader().setResizeMode(2, QHeaderView.ResizeToContents)

		self.ui.projectScopeRadioButton.setChecked(local)
		self.ui.globalScopeRadioButton.setChecked(not local)

		self.connect(self.ui.newParameterButton, SIGNAL("clicked()"), self.newParameter)
		self.connect(self.ui.removeParameterButton, SIGNAL("clicked()"), self.removeParameter)
		self.connect(self.ui.okCancelButtons, SIGNAL("accepted()"), self.finished)

	def newParameter(self):
		numParams = self.ui.parameterList.rowCount()
		self.ui.parameterList.insertRow(numParams)

	def removeParameter(self):
		row = self.ui.parameterList.currentRow()

		if row != -1:
			self.ui.parameterList.removeRow(row)

	def finished(self):
		# If a callback function was defined, call it
		if self.callback:
			# Construct a Module object to return
			module = Module(str(self.ui.nameInputBox.text()))
			module.addCommand(str(self.ui.commandInputBox.text()))
			for i in xrange(0, self.ui.parameterList.rowCount()):
				list = self.ui.parameterList
				param = Parameter()
				param.id = str(list.item(i, 0).text())
				param.description = str(list.item(i, 1).text())
				param.value = str(list.item(i, 2).text())
				module.addParameter(param)

			self.callback(module, self.local)
