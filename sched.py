#!/usr/bin/env python

import sys
import os
from PyQt4 import QtGui, QtCore
from forms import Ui_MainWindow
from forms import Ui_ModuleListWidget

class FrmMainWindow(QtGui.QMainWindow):

	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)		
		self.ui = Ui_MainWindow.Ui_MainWindow()
		self.ui.setupUi(self)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = FrmMainWindow()
	window.show()

	# Load in the list of global modules
	try:
		os.listdir(os.path.expanduser('~') + os.sep + ".sched")
		input = open(os.path.expanduser('~') + os.sep + ".sched/modules.xml", "r")
		xml = input.read()
		from imports import ModuleXMLParser
		parser = ModuleXMLParser.ModuleXMLParser()
		modules = parser.parse(xml)
		for param in modules.parameters:
			window.ui.listWidget.addItem(QtGui.QListWidgetItem(param.value))				
	except OSError:
		print "Warning: ~/.sched doesn't exist. Attempting to create it."
		try:
			os.mkdir(os.path.expanduser('~') + os.sep + ".sched")
			print "Success."
		except OSError:
			print "Error! Can't write to the home directory."

	
	sys.exit(app.exec_())
