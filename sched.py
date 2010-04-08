#!/usr/bin/env python

import sys
from PyQt4.QtGui import QApplication
from forms.mainwindow import MainWindow

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()

#	from forms.modulelistwidget import ModuleListWidgetItem

#        ui = ModuleListWidgetItem(window.ui.listWidget)
#        widget.show()
#	window.ui.listWidget.addItem(ui)

	sys.exit(app.exec_())
