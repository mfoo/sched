#!/usr/bin/env python

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from forms import MainWindow

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow.MainWindow()
	window.show()
	window.loadGlobals()
	sys.exit(app.exec_())

