"""
This module contains the NewModuleWidget class, which allows for adding a new
module into Sched
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QHeaderView
from PyQt4.QtCore import SIGNAL
from forms.ui_newmodulewizard import Ui_Dialog
from imports.Module import Module
from imports.Parameter import Parameter

class NewModuleWizard(QDialog):
    """
    NewModuleWizard allows you to enter details of a new module. Passing
    local=True will add it to the current project, local=False will add it to
    the context
    """
    def __init__(self, parent=None, local=True, callback=True):
        QDialog.__init__(self, parent)

        self.callback = callback
        self.local = local
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.parameterList.horizontalHeader().setResizeMode(0,
            QHeaderView.ResizeToContents)
        self.ui.parameterList.horizontalHeader().setResizeMode(1,
            QHeaderView.Stretch)
        self.ui.parameterList.horizontalHeader().setResizeMode(2,
            QHeaderView.ResizeToContents)

        self.connect(self.ui.newParameterButton, SIGNAL("clicked()"),
            self.newParameter)
        self.connect(self.ui.removeParameterButton, SIGNAL("clicked()"),
            self.removeParameter)
        self.connect(self.ui.okCancelButtons, SIGNAL("accepted()"),
            self.finished)

    def newParameter(self):
        """
        Called when the new parameter button is clicked in the UI, adds an
        extra row to the parameter table
        """
        numParams = self.ui.parameterList.rowCount()
        self.ui.parameterList.insertRow(numParams)

    def removeParameter(self):
        """
        Removes the selected row in the parameter table
        """
        row = self.ui.parameterList.currentRow()

        if row != -1:
            self.ui.parameterList.removeRow(row)

    def finished(self):
        """
        Called when the user clicks "OK". Creates the module and adds it to the
        right place
        """
        # If a callback function was defined, call it
        if self.callback:
            parameters = []
            # Construct a Module object to return
            module = Module(str(self.ui.nameInputBox.text()))
            module.add_command(str(self.ui.commandInputBox.text()))
            for i in xrange(0, self.ui.parameterList.rowCount()):
                try:
                    list = self.ui.parameterList
                    param = Parameter()
                    param.param_id = str(list.item(i, 0).text())
                    param.description = str(list.item(i, 1).text())
                    param.value = str(list.item(i, 2).text())
                    parameters.append(param)
                except AttributeError:
                    # They missed some input data, ignore this param
                    pass

            self.callback(module, parameters, self.local)
