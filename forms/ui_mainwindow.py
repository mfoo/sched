# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/mainwindow.ui'
#
# Created: Thu Apr 29 22:40:51 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 809)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.contentWrapper = QtGui.QHBoxLayout()
        self.contentWrapper.setObjectName("contentWrapper")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.specialModulesLabel = QtGui.QLabel(self.centralWidget)
        self.specialModulesLabel.setObjectName("specialModulesLabel")
        self.verticalLayout_6.addWidget(self.specialModulesLabel)
        self.specialModulesList = QtGui.QListWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.specialModulesList.sizePolicy().hasHeightForWidth())
        self.specialModulesList.setSizePolicy(sizePolicy)
        self.specialModulesList.setMaximumSize(QtCore.QSize(150, 60))
        self.specialModulesList.setObjectName("specialModulesList")
        self.verticalLayout_6.addWidget(self.specialModulesList)
        self.verticalLayout_2.addLayout(self.verticalLayout_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.contextLabel = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contextLabel.sizePolicy().hasHeightForWidth())
        self.contextLabel.setSizePolicy(sizePolicy)
        self.contextLabel.setObjectName("contextLabel")
        self.horizontalLayout_4.addWidget(self.contextLabel)
        self.currentContextName = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentContextName.sizePolicy().hasHeightForWidth())
        self.currentContextName.setSizePolicy(sizePolicy)
        self.currentContextName.setObjectName("currentContextName")
        self.horizontalLayout_4.addWidget(self.currentContextName)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.contextModuleList = QtGui.QListWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contextModuleList.sizePolicy().hasHeightForWidth())
        self.contextModuleList.setSizePolicy(sizePolicy)
        self.contextModuleList.setMinimumSize(QtCore.QSize(0, 0))
        self.contextModuleList.setMaximumSize(QtCore.QSize(150, 16777215))
        self.contextModuleList.setDragEnabled(True)
        self.contextModuleList.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.contextModuleList.setObjectName("contextModuleList")
        self.verticalLayout_2.addWidget(self.contextModuleList)
        self.newGlobalModuleButton = QtGui.QPushButton(self.centralWidget)
        self.newGlobalModuleButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.newGlobalModuleButton.setObjectName("newGlobalModuleButton")
        self.verticalLayout_2.addWidget(self.newGlobalModuleButton)
        self.contentWrapper.addLayout(self.verticalLayout_2)
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.contentWrapper.addWidget(self.line)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mappingsVerticalWrapper = QtGui.QVBoxLayout()
        self.mappingsVerticalWrapper.setObjectName("mappingsVerticalWrapper")
        self.globalMappingsLabel = QtGui.QLabel(self.centralWidget)
        self.globalMappingsLabel.setObjectName("globalMappingsLabel")
        self.mappingsVerticalWrapper.addWidget(self.globalMappingsLabel)
        self.mappingsTable = QtGui.QTableWidget(self.centralWidget)
        self.mappingsTable.setAutoFillBackground(True)
        self.mappingsTable.setAlternatingRowColors(True)
        self.mappingsTable.setCornerButtonEnabled(False)
        self.mappingsTable.setObjectName("mappingsTable")
        self.mappingsTable.setColumnCount(3)
        self.mappingsTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.mappingsTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.mappingsTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.mappingsTable.setHorizontalHeaderItem(2, item)
        self.mappingsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.mappingsTable.horizontalHeader().setDefaultSectionSize(100)
        self.mappingsTable.horizontalHeader().setMinimumSectionSize(10)
        self.mappingsTable.horizontalHeader().setStretchLastSection(True)
        self.mappingsTable.verticalHeader().setVisible(False)
        self.mappingsVerticalWrapper.addWidget(self.mappingsTable)
        self.verticalLayout_3.addLayout(self.mappingsVerticalWrapper)
        self.projectModulesLabel = QtGui.QLabel(self.centralWidget)
        self.projectModulesLabel.setObjectName("projectModulesLabel")
        self.verticalLayout_3.addWidget(self.projectModulesLabel)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.projectVerticalWrapper = QtGui.QVBoxLayout()
        self.projectVerticalWrapper.setObjectName("projectVerticalWrapper")
        self.moduleList = QtGui.QTreeWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.moduleList.sizePolicy().hasHeightForWidth())
        self.moduleList.setSizePolicy(sizePolicy)
        self.moduleList.setAcceptDrops(True)
        self.moduleList.setDragEnabled(True)
        self.moduleList.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.moduleList.setAlternatingRowColors(True)
        self.moduleList.setObjectName("moduleList")
        self.moduleList.header().setCascadingSectionResizes(False)
        self.moduleList.header().setDefaultSectionSize(100)
        self.moduleList.header().setHighlightSections(True)
        self.moduleList.header().setMinimumSectionSize(50)
        self.moduleList.header().setStretchLastSection(True)
        self.projectVerticalWrapper.addWidget(self.moduleList)
        self.horizontalLayout_5.addLayout(self.projectVerticalWrapper)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.deleteModuleButton = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteModuleButton.sizePolicy().hasHeightForWidth())
        self.deleteModuleButton.setSizePolicy(sizePolicy)
        self.deleteModuleButton.setObjectName("deleteModuleButton")
        self.verticalLayout_4.addWidget(self.deleteModuleButton)
        self.newProjectModuleButton = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newProjectModuleButton.sizePolicy().hasHeightForWidth())
        self.newProjectModuleButton.setSizePolicy(sizePolicy)
        self.newProjectModuleButton.setObjectName("newProjectModuleButton")
        self.verticalLayout_4.addWidget(self.newProjectModuleButton)
        self.addToContextButton = QtGui.QPushButton(self.centralWidget)
        self.addToContextButton.setObjectName("addToContextButton")
        self.verticalLayout_4.addWidget(self.addToContextButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.moduleEditWrapper = QtGui.QFormLayout()
        self.moduleEditWrapper.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.moduleEditWrapper.setObjectName("moduleEditWrapper")
        self.nameLabel = QtGui.QLabel(self.centralWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.moduleEditWrapper.setWidget(0, QtGui.QFormLayout.LabelRole, self.nameLabel)
        self.nameEdit = QtGui.QLineEdit(self.centralWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.moduleEditWrapper.setWidget(0, QtGui.QFormLayout.FieldRole, self.nameEdit)
        self.commandLabel = QtGui.QLabel(self.centralWidget)
        self.commandLabel.setObjectName("commandLabel")
        self.moduleEditWrapper.setWidget(1, QtGui.QFormLayout.LabelRole, self.commandLabel)
        self.commandEdit = QtGui.QTextEdit(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.commandEdit.sizePolicy().hasHeightForWidth())
        self.commandEdit.setSizePolicy(sizePolicy)
        self.commandEdit.setObjectName("commandEdit")
        self.moduleEditWrapper.setWidget(1, QtGui.QFormLayout.FieldRole, self.commandEdit)
        self.descriptionLabel = QtGui.QLabel(self.centralWidget)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.moduleEditWrapper.setWidget(2, QtGui.QFormLayout.LabelRole, self.descriptionLabel)
        self.descriptionEdit = QtGui.QLineEdit(self.centralWidget)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.moduleEditWrapper.setWidget(2, QtGui.QFormLayout.FieldRole, self.descriptionEdit)
        self.dependenciesLabel = QtGui.QLabel(self.centralWidget)
        self.dependenciesLabel.setObjectName("dependenciesLabel")
        self.moduleEditWrapper.setWidget(3, QtGui.QFormLayout.LabelRole, self.dependenciesLabel)
        self.dependencyEdit = QtGui.QLineEdit(self.centralWidget)
        self.dependencyEdit.setObjectName("dependencyEdit")
        self.moduleEditWrapper.setWidget(3, QtGui.QFormLayout.FieldRole, self.dependencyEdit)
        self.verticalLayout_3.addLayout(self.moduleEditWrapper)
        self.executeButton = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.executeButton.sizePolicy().hasHeightForWidth())
        self.executeButton.setSizePolicy(sizePolicy)
        self.executeButton.setMinimumSize(QtCore.QSize(150, 0))
        self.executeButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.executeButton.setObjectName("executeButton")
        self.verticalLayout_3.addWidget(self.executeButton)
        self.contentWrapper.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.contentWrapper)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1123, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen_Project = QtGui.QAction(MainWindow)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.actionClose_Project = QtGui.QAction(MainWindow)
        self.actionClose_Project.setObjectName("actionClose_Project")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave_Project = QtGui.QAction(MainWindow)
        self.actionSave_Project.setObjectName("actionSave_Project")
        self.actionSave_Context = QtGui.QAction(MainWindow)
        self.actionSave_Context.setObjectName("actionSave_Context")
        self.actionLoad_Context = QtGui.QAction(MainWindow)
        self.actionLoad_Context.setObjectName("actionLoad_Context")
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addAction(self.actionLoad_Context)
        self.menuFile.addAction(self.actionSave_Context)
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Sched Flow Editor", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setStatusTip(QtGui.QApplication.translate("MainWindow", "Run the current project", None, QtGui.QApplication.UnicodeUTF8))
        self.specialModulesLabel.setText(QtGui.QApplication.translate("MainWindow", "Special Modules", None, QtGui.QApplication.UnicodeUTF8))
        self.specialModulesList.setToolTip(QtGui.QApplication.translate("MainWindow", "A list of available special modules", None, QtGui.QApplication.UnicodeUTF8))
        self.contextLabel.setText(QtGui.QApplication.translate("MainWindow", "Context:", None, QtGui.QApplication.UnicodeUTF8))
        self.currentContextName.setText(QtGui.QApplication.translate("MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.contextModuleList.setToolTip(QtGui.QApplication.translate("MainWindow", "A list of modules that are available from the current loaded context", None, QtGui.QApplication.UnicodeUTF8))
        self.newGlobalModuleButton.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add a new module to this context", None, QtGui.QApplication.UnicodeUTF8))
        self.newGlobalModuleButton.setText(QtGui.QApplication.translate("MainWindow", "New Context Module", None, QtGui.QApplication.UnicodeUTF8))
        self.globalMappingsLabel.setText(QtGui.QApplication.translate("MainWindow", "Global Mappings", None, QtGui.QApplication.UnicodeUTF8))
        self.mappingsTable.setStatusTip(QtGui.QApplication.translate("MainWindow", "A list of project variables and that they translate to", None, QtGui.QApplication.UnicodeUTF8))
        self.mappingsTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Symbol", None, QtGui.QApplication.UnicodeUTF8))
        self.mappingsTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.mappingsTable.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Mapping", None, QtGui.QApplication.UnicodeUTF8))
        self.projectModulesLabel.setText(QtGui.QApplication.translate("MainWindow", "Project Modules", None, QtGui.QApplication.UnicodeUTF8))
        self.moduleList.setToolTip(QtGui.QApplication.translate("MainWindow", "A list of modules that are contained in this project", None, QtGui.QApplication.UnicodeUTF8))
        self.moduleList.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.moduleList.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.moduleList.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Command", None, QtGui.QApplication.UnicodeUTF8))
        self.moduleList.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.moduleList.headerItem().setText(4, QtGui.QApplication.translate("MainWindow", "Dependencies", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteModuleButton.setText(QtGui.QApplication.translate("MainWindow", "Delete Module", None, QtGui.QApplication.UnicodeUTF8))
        self.newProjectModuleButton.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add a new module to this project", None, QtGui.QApplication.UnicodeUTF8))
        self.newProjectModuleButton.setText(QtGui.QApplication.translate("MainWindow", "New Project Module", None, QtGui.QApplication.UnicodeUTF8))
        self.addToContextButton.setText(QtGui.QApplication.translate("MainWindow", "Add To Context", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("MainWindow", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.nameEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "The name of the current module", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLabel.setText(QtGui.QApplication.translate("MainWindow", "Command:", None, QtGui.QApplication.UnicodeUTF8))
        self.commandEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "The command that will be executed. Any symbol from the above list will be substituted for it\'s mapping upon execution.", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionLabel.setText(QtGui.QApplication.translate("MainWindow", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "The description of the current module", None, QtGui.QApplication.UnicodeUTF8))
        self.dependenciesLabel.setText(QtGui.QApplication.translate("MainWindow", "Dependencies:", None, QtGui.QApplication.UnicodeUTF8))
        self.dependencyEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "The IDs of the modules that must be executed before this module", None, QtGui.QApplication.UnicodeUTF8))
        self.executeButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Start the processing of these modules", None, QtGui.QApplication.UnicodeUTF8))
        self.executeButton.setText(QtGui.QApplication.translate("MainWindow", "Execute", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Project.setText(QtGui.QApplication.translate("MainWindow", "Load Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_Project.setText(QtGui.QApplication.translate("MainWindow", "Close Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Project.setText(QtGui.QApplication.translate("MainWindow", "Save Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Context.setText(QtGui.QApplication.translate("MainWindow", "Save Context", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Context.setText(QtGui.QApplication.translate("MainWindow", "Load Context", None, QtGui.QApplication.UnicodeUTF8))

