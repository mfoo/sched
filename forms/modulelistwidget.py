"""
This module contains the ModuleListWidgetItem class which is used to show
relevant information to a module in the modules list.
"""
from PyQt4.QtGui import QListWidgetItem
from PyQt4.QtCore import QString

class ModuleListWidgetItem(QListWidgetItem):
    """
    This class is a custom widget that allows a custom display of Modules
    """
    def __init__(self, module, parent=None):
        QListWidgetItem.__init__(self, parent, QListWidgetItem.UserType)
        self.parent = parent
       	self.module = module
        self.setToolTip(QString(module.description))
        self.setStatusTip(QString(module.description))
        self.setText(QString(module.name))
