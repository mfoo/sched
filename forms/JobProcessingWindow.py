from PyQt4.QtCore import *
from PyQt4.QtGui import *
from forms.Ui_JobProcessingWindow import Ui_Dialog

class JobProcessingWindow(QDialog):
    def __init__(self, parent=None):
	QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
