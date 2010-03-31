from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QHeaderView
from PyQt4.QtGui import QTableWidgetItem
from PyQt4.QtGui import QFileDialog

from PyQt4.QtCore import QMimeData
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QString

from copy import deepcopy
from string import replace

import os
import re

from forms.ui_mainwindow import Ui_MainWindow
from forms.ui_modulelistwidget import Ui_ModuleListWidget

from imports import Module, Parameter

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Variable to decided whether or not something has been changed this
        # session or not
        self.changed = False

        # Configure individual column widths
        self.ui.mappingsTable.horizontalHeader().setResizeMode(0,
            QHeaderView.ResizeToContents)
        self.ui.mappingsTable.horizontalHeader().setResizeMode(1,
            QHeaderView.Stretch)
        self.ui.mappingsTable.horizontalHeader().setResizeMode(2,
            QHeaderView.ResizeToContents)

        # Connect signal handlers for UI events
        self.connect(self.ui.listWidget, \
            SIGNAL("itemClicked(QListWidgetItem*)"), \
            self.globalModuleListClickHandler)
        self.connect(self.ui.projectModuleList, \
            SIGNAL("itemClicked(QListWidgetItem*)"), \
            self.projectModuleListClickHandler)
        self.connect(self.ui.actionOpen_Project, \
            SIGNAL("activated()"), \
            self.openFileClicked)
        self.connect(self.ui.actionSave_Project, \
            SIGNAL("activated()"), \
            self.saveProjectClicked)
        self.connect(self.ui.actionExit, \
            SIGNAL("activated()"), \
            self.closeProject)
        self.connect(self.ui.actionSave_Context, \
            SIGNAL("activated()"), \
            self.saveContextClicked)
        self.connect(self.ui.actionLoad_Context, \
            SIGNAL("activated()"), \
            self.loadContextClicked)
        self.connect(self.ui.executeButton, \
            SIGNAL("clicked()"), \
            self.execute)
        self.connect(self.ui.newGlobalModuleButton, \
            SIGNAL("clicked()"), \
            self.globalModuleButtonClicked)
        self.connect(self.ui.newProjectModuleButton, \
            SIGNAL("clicked()"), \
            self.projectModuleButtonClicked)
        self.connect(self.ui.commandEdit, \
            SIGNAL("textChanged()"), \
            self.moduleCommandTextChanged)

        # Configure the column headings for the variable mappings table
        headers = ["Symbol", "Description", "Mapping"]
        self.ui.mappingsTable.setColumnCount(len(headers))
        self.ui.mappingsTable.setHorizontalHeaderLabels(headers)
        
        # Load the global modules
        # TODO: Delete loadGlobals
        # self.loadGlobals()
        self.contextName = "test"
        self.updateCurrentContextName()

    def updateCurrentContextName(self):
        self.ui.currentContextName.setText(QString(self.contextName))

    def moduleCommandTextChanged(self):
        """
        Called when the user changes a command.
        Should check if the user has made a change to a module and should update
        the internal representation of that module to reflect it.
        """
        # Set the text of the module to contain the text of the command edit
        text = str(self.ui.commandEdit.toPlainText())
        currentModule = self.ui.projectModuleList.currentItem()
        currentModule.module.command = text
        self.changed = True

    def openFileClicked(self):
        """
        Displays a file dialog to get the filename of the file to save to
        """
        fileName = QFileDialog.getOpenFileName(self, "Open File",
            os.path.expanduser("~") + "/.sched/projects/", "Sched files (*)")

        if fileName:
            self.loadProject(fileName)

    def execute(self):
        """
        Executes the current project
        """
        from imports.ProcessHandler import ProcessHandler
        from imports.process import Process
        modules = [self.ui.projectModuleList.item(x).module for x in xrange(0, \
            self.ui.projectModuleList.count())]
        processes = []
        for module in modules:
            command = module.command
            for param in module.parameters:
                command = replace(command, param.param_id, param.value)
                command = "sleep 5"
            processes.append(Process(command))
            
        self.handler = ProcessHandler(processes)

        self.handler.ui.show()
       
        self.handler.start()

    def loadContextClicked(self):
        """
        Called when the user clicks "Load Context" from the menu. Opens a file
        dialog to get the path then loads the context into the context pane
        """
        fileName = QFileDialog.getOpenFileName(self, "Open Context File",
            os.path.expanduser("~") + "/.sched/contexts", "Sched files (*)")

        if not fileName:
            return
        
        try:
            input = open(fileName, "r")
            xml = input.read()
            modules = self.parseXML(xml)
            from forms.ui_modulelistwidget import Ui_ModuleListWidget
            for module in modules:
                ui = Ui_ModuleListWidget(module,parent = self.ui.listWidget)
                self.ui.listWidget.addItem(ui)

            self.updateMappings()

            name = re.search('.*/(.*)\..*', fileName)
            self.contextName = name.group(1)
            self.updateCurrentContextName()
        except OSError:
            result = self.okToContinue("Error.", "~/.sched doesn't exist. " + \
                "This means that global modules cannot be saved. Created it?")
            if result:
                try:
                    os.mkdir(os.path.expanduser('~') + os.sep + ".sched")
                except OSError:
                    
                    print "Error! Can't write to the home directory."
                    
    def saveContextClicked(self):
        """
        Called when the user requests to save the current context. Constructs
        the relevant XML and saves to the context's file
        """
        modules = [self.ui.listWidget.item(x).module for x in xrange(0, \
            self.ui.listWidget.count())]
        from xml.dom.minidom import Document
        doc = Document()
        list = doc.createElement("moduleList")
        doc.appendChild(list)
        for module in modules:
            mod = doc.createElement("module")
            mod.setAttribute("name", module.name)
            description = doc.createElement("description")
            descriptiontext = doc.createTextNode(module.description)
            description.appendChild(descriptiontext)

            command = doc.createElement("command")
            commandtext = doc.createTextNode(module.command)
            command.appendChild(commandtext)

            mod.appendChild(description)
            mod.appendChild(command)

            parameters = doc.createElement("parameters")
            
            for param in module.parameters:
                parameter = doc.createElement("param")

                id = doc.createElement("id")
                idtext = doc.createTextNode(param.param_id)
                id.appendChild(idtext)

                descrip = doc.createElement("description")
                descriptext = doc.createTextNode(param.description)
                descrip.appendChild(descriptext)

                value = doc.createElement("value")
                valuetext = doc.createTextNode(param.value)
                value.appendChild(valuetext)

                parameter.appendChild(id)
                parameter.appendChild(descrip)
                parameter.appendChild(value)

                parameters.appendChild(parameter)

            mod.appendChild(parameters)

            list.appendChild(mod)

        prettyxml = doc.toprettyxml(indent="  ")

        fileName = os.path.expanduser("~") + "/.sched/contexts/" + \
            self.contextName
        # TODO: Check if the file exists, don't overwrite it
        if fileName:
            file = open(fileName, "w")
            file.write(prettyxml)
            file.close()

    def saveProjectClicked(self):
        """
        Called when the user clicks save project. Constructs the relevant XML,
        requests a filename and writes the file
        """
        # TODO: Add the context that the project is using
        
        modules = [self.ui.projectModuleList.item(x).module for x in xrange(0, \
            self.ui.projectModuleList.count())]
        from xml.dom.minidom import Document
        doc = Document()
        list = doc.createElement("moduleList")
        doc.appendChild(list)
        for module in modules:
            mod = doc.createElement("module")
            mod.setAttribute("name", module.name)
            description = doc.createElement("description")
            descriptiontext = doc.createTextNode(module.description)
            description.appendChild(descriptiontext)

            command = doc.createElement("command")
            commandtext = doc.createTextNode(module.command)
            command.appendChild(commandtext)

            mod.appendChild(description)
            mod.appendChild(command)

            parameters = doc.createElement("parameters")
            
            for param in module.parameters:
                parameter = doc.createElement("param")

                id = doc.createElement("id")
                idtext = doc.createTextNode(param.param_id)
                id.appendChild(idtext)

                descrip = doc.createElement("description")
                descriptext = doc.createTextNode(param.description)
                descrip.appendChild(descriptext)

                value = doc.createElement("value")
                valuetext = doc.createTextNode(param.value)
                value.appendChild(valuetext)

                parameter.appendChild(id)
                parameter.appendChild(descrip)
                parameter.appendChild(value)

                parameters.appendChild(parameter)

            mod.appendChild(parameters)

            list.appendChild(mod)

        prettyxml = doc.toprettyxml(indent="  ")

        fileName = QFileDialog.getSaveFileName(self, "Save File", \
            os.path.expanduser("~") + ".sched/projects/", "Sched files (*)")
        # TODO: Check if the file exists, don't overwrite it
        if fileName:
            file = open(fileName, "w")
            file.write(prettyxml)
            file.close()


    def loadProject(self, fileName):
        """
        Called when the user clicks load project. Loads a file and parses it
        """
        # TODO: When the context is in the project file, load the context as
        # well as the modules for this project
        try:
            input = open(fileName)
            xml = input.read()
            modules = self.parseXML(xml)
            from forms.ui_modulelistwidget import Ui_ModuleListWidget
            for module in modules:
                # Add the module to the list
                ui = Ui_ModuleListWidget(module, \
                    parent=self.ui.projectModuleList)
                self.ui.projectModuleList.addItem(ui)
                
                # Add the module's parameters to the parameter list
            self.updateMappings()
        except OSError:
            # TODO: Make an error message
            print "Can't load project."

    def parseXML(self, xml):
        """
        Parse the XML file
        """
        from imports.ModuleXMLParser import ModuleXMLParser
        parser = ModuleXMLParser()
        return parser.parse(xml)

    def loadGlobals(self):
        """
        Load and parse the global modules into the global list
        """
        try:
            input = open(os.path.expanduser('~') + os.sep + \
                ".sched/modules.xml", "r")
            xml = input.read()
            modules = self.parseXML(xml)
            from forms.ui_modulelistwidget import Ui_ModuleListWidget
            for module in modules:
                ui = Ui_ModuleListWidget(module,parent = self.ui.listWidget)
                self.ui.listWidget.addItem(ui)

            self.updateMappings()

        except OSError:
            result = self.okToContinue("Error.", "~/.sched doesn't exist. " + \
                "This means that global modules cannot be saved. Created it?")
            if result:
                try:
                    os.mkdir(os.path.expanduser('~') + os.sep + ".sched")
                except OSError:
                    
                    print "Error! Can't write to the home directory."

    def closeProject(self):
        """
        Close the current project
        """
        if self.changed:
            result = self.okToContinue("Error.", \
                "There are unsaved changes. Save them?")
            if result:
                # TODO: Save
                print "Write this"
                self.saveProject()
                self.close()
        else:
            self.close()

    def okToContinue(self, title, message):
        """
        Generic method that pops up a dialog asking if it's OK to continue with
        the specified message
        """
        reply = QMessageBox.question(self, title, message, \
            QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
        if reply == QMessageBox.Cancel:
            return False
        elif reply == QMessageBox.Yes:
            return True


    def globalModuleButtonClicked(self):
        """
        Shows a 'New Module' wizard that creates a global module (all projects)
        """
        self.showNewModuleWizard(False)

    def projectModuleButtonClicked(self):
        """
        Shows a 'New Module' wizard that creates a local module (this
        project only)
        """
        self.showNewModuleWizard(True)
    

    def showNewModuleWizard(self, type):
        """
        Shows the wizard dialog that allows creating a new module
        """
        from forms.newmodulewizard import NewModuleWizard
        self.newModuleWizard = NewModuleWizard(parent = self, local = type, \
            callback = self.addNewModule)
        self.newModuleWizard.show()

    def addNewModule(self, module, local):
        """
        Function called by the new module wizard to add the new module to the
        current project
        """
        # TODO: This should not be here, showNewModule should return a module
        # object, not be passed a callback
        
        # TODO: Remove prints
        print module.command
        print module.name
        print module.description
        for param in module.parameters:
            print param.param_id
            print param.description
            print param.value
        self.ui.listWidget.addItem(Ui_ModuleListWidget(module))
        self.updateMappings()

    def updateMappings(self):
        """
        Repopulates the table of symbol -> description + mapping and is called
        whenever a change is made to the modules
        """
        dataType = QMimeData()
        modules = [self.ui.projectModuleList.item(x).module for x in xrange(0, \
            self.ui.projectModuleList.count())]
        self.ui.mappingsTable.setSortingEnabled(False)
        self.ui.mappingsTable.setRowCount(sum([len(x.parameters) for x in \
            modules]) +1)

        counter = 0
        for module in modules:
            for param in module.parameters:
                self.ui.mappingsTable.setItem(counter, 0, \
                    QTableWidgetItem(QString(param.param_id)))
                self.ui.mappingsTable.setItem(counter, 1, \
                    QTableWidgetItem(QString(param.description)))
                self.ui.mappingsTable.setItem(counter, 2, \
                    QTableWidgetItem(QString(param.value)))
                counter += 1

        self.ui.mappingsTable.setSortingEnabled(True)
    
    def globalModuleListClickHandler(self, item):
        """
        Called when the user clicks the global module list. Makes a copy of the
        module that was clicked on and adds it to the current project as a local
        module
        """
        # Check if the module being loaded redefines any current parameter
        # TODO: If it does then rename it in the command and parameter part.
        modules = [self.ui.projectModuleList.item(x).module for x in xrange(0, \
            self.ui.projectModuleList.count())]
        for module in modules:
            for parameter in module.parameters:
                for newParameter in item.module.parameters:
                    if parameter == newParameter:
                        # TODO: Add the name of the module to the param name?
                        # Use a number?
                        print "temp"

        self.changed = True
        newmodule = deepcopy(item)                
        self.ui.projectModuleList.addItem(Ui_ModuleListWidget(newmodule.module))
        self.updateMappings()

    def projectModuleListClickHandler(self, item):
        """
        When a module is clicked on in the current project list,
        populate the command line box with it's command.
        """
        self.ui.commandEdit.setText(QString(item.module.command))
