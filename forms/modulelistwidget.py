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

class GroupWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
#        self.setAcceptDrops(True)
        self.dropTarget = False

    def dragEnterEvent(self, event):
        self.dropTarget = True
        print "enter" + self.parent.module.name

    def dragLeaveEvent(self, event):
        self.dropTarget = False 

#    def dropEvent(self, event):
#        print "drop event"
#        dragItem = event.source()
#        dragItem.generateWidget(dragItem.module.name, \
#            dragItem.module.description)
#
#        newLabel = QLabel(QString(dragItem.module.name))
#        self.layout.addWidget(newLabel)
        

class ModuleListWidgetItem(QListWidgetItem):
    """
    This class is a custom widget that allows a custom display of Modules
    """
    def __init__(self, module, parent=None):
        QListWidgetItem.__init__(self, parent, QListWidgetItem.UserType)
        self.parent = parent
       	self.module = module
#        self.widget.setAcceptDrops(True)

#        self.widget.p = self
        self.nameLabel = QLabel(QString(module.name))
        self.descriptionLabel = QLabel(QString("    " + module.description))

        self.generateWidget(module.name, module.description)
 
    def generateWidget(self, name, description):
#        self.widget = QWidget()
        self.widget = GroupWidget()
        self.layout = QVBoxLayout(self.widget)
        self.layout.addWidget(self.nameLabel)
        self.layout.addWidget(self.descriptionLabel)

#        self.setSizeHint(QSize(0, self.widget.minimumHeight()))
#        maxHeight = self.nameLabel.height() * 2
        maxHeight = 80
        self.setSizeHint(QSize(0, maxHeight))
        self.widget.setFixedHeight(80)

 #       self.widget.setAcceptDrops(True)
#        self.widget.setDragEnabled(True)
        self.parent.setItemWidget(self, self.widget)

 #       self.model = 

    def dragEnterEvent(self, e):
        e.accept()


