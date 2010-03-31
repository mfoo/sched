#!/usr/bin/env python

import sys
from PyQt4.QtGui import QApplication
from forms.mainwindow import MainWindow

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
