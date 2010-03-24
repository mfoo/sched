#!/usr/bin/env python

import sys
import os
#from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
#from forms import Ui_MainWindow
from forms import MainWindow
#from forms import Ui_ModuleListWidget
#from forms import ModuleListWidgetItem

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow.MainWindow()
	window.show()

	# Load in the list of global modules
	try:
		os.listdir(os.path.expanduser('~') + os.sep + ".sched")
		input = open(os.path.expanduser('~') + os.sep + ".sched/modules.xml", "r")
		xml = input.read()
		from imports import ModuleXMLParser
		parser = ModuleXMLParser.ModuleXMLParser()
		modules = parser.parse(xml)
		from forms import Ui_ModuleListWidget
		for module in modules:
			ui = Ui_ModuleListWidget.Ui_ModuleListWidget(module,parent = window.ui.listWidget)
			window.ui.listWidget.addItem(ui)
			
		window.updateMappings()

	except OSError:
		print "Warning: ~/.sched doesn't exist. Attempting to create it."
		try:
			os.mkdir(os.path.expanduser('~') + os.sep + ".sched")
			print "Success."
		except OSError:
			print "Error! Can't write to the home directory."
			sys.exit(1)

	
	sys.exit(app.exec_())
