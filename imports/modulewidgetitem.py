from PyQt4.QtGui import QTreeWidgetItem

from PyQt4.QtCore import Qt
from PyQt4.QtCore import QString

from imports.Module import Module

class ModuleWidgetItem(QTreeWidgetItem, Module):
    """
    This class represents a Module that can be displayed as an item in a module
    list.
    """
    def __init__(self, module, parent=None):
        QTreeWidgetItem.__init__(self, parent)
        Module.__init__(self)
        self.type = ""
        self.setModule(module)
        self.updateUi()

    def setModule(self, module):
        """
        Give this widgetitem an existing module to represent.
        """
        self.add_description(module.description)
        self.add_name(module.name)
        self.add_command(module.command)
        for param in module.parameters:
            self.add_parameter(param)

    def updateUi(self):
        # TODO: Implement IDs
        self.setData(0, Qt.DisplayRole, 1)
        self.setData(1, Qt.DisplayRole, QString(self.name))
        self.setData(2, Qt.DisplayRole, QString(self.command))
        self.setData(3, Qt.DisplayRole, QString(self.description))
        # TODO: Allow dependencies
        self.setData(4, Qt.DisplayRole, QString("None"))
