"""
This module contains the ModuleListWidgetItem class
"""

#from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QListWidgetItem
import Ui_ModuleListWidget

class ModuleListWidgetItem(QListWidgetItem):
    """
    This class is a custom widget that allows a custom display of Modules
    """
    def __init__(self, parent=None):
        QListWidgetItem.__init__(self, parent, 10000)
        self.ui = Ui_ModuleListWidget.Ui_ModuleListWidget()
        self.ui.setupUi(self)
