"""
This module contains the ModuleListWidgetItem class which is used to show
relevant information to a module in the modules list. It subclasses
QListWidgetItem in order to provide more than just one text string as
QListWidgetItem allows.
"""

from PyQt4.QtGui import QListWidgetItem
from PyQt4.QtGui import QPushButton
from PyQt4.QtCore import QRect
from PyQt4.QtCore import QString
from PyQt4.QtCore import QSize
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QWidget

class ModuleListWidgetItem(QListWidgetItem):
    """
    This class is a custom widget that allows a custom display of Modules
    """
    def __init__(self, module, parent=None):
        QListWidgetItem.__init__(self, parent, QListWidgetItem.UserType)
       	self.module = module
        self.widget = QWidget()

        self.nameLabel = QLabel(QString(module.name))
        self.descriptionLabel = QLabel(QString("    " + module.description))

        self.layout = QVBoxLayout(self.widget)
        self.layout.addWidget(self.nameLabel)
        self.layout.addWidget(self.descriptionLabel)

#        self.setSizeHint(QSize(0, self.widget.minimumHeight()))
#        maxHeight = self.nameLabel.height() * 2
        maxHeight = 80
        self.setSizeHint(QSize(0, maxHeight))
        self.widget.setFixedHeight(80)
        parent.setItemWidget(self, self.widget)
