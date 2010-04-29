from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QHeaderView
from PyQt4.QtGui import QAbstractItemView
from PyQt4.QtGui import QTableWidgetItem
from PyQt4.QtGui import QTreeWidgetItem
from PyQt4.QtGui import QFileDialog
from PyQt4.QtGui import QListWidget
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QListWidgetItem
from PyQt4.QtGui import QMessageBox

from PyQt4.QtCore import QMimeData
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QString
from PyQt4.QtCore import QStringList
from PyQt4.QtCore import QRect
from PyQt4.QtCore import Qt

from copy import deepcopy
from string import replace
from types import IntType
from types import ListType

import os
import re

from forms.ui_mainwindow import Ui_MainWindow
from forms.modulelistwidget import ModuleListWidgetItem

from imports import Module, Parameter
from imports.modulewidgetitem import ModuleWidgetItem

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
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
        self.connect(self.ui.contextModuleList, \
            SIGNAL("itemClicked(QListWidgetItem*)"), \
            self.globalModuleListClickHandler)
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
        self.connect(self.ui.deleteModuleButton, \
            SIGNAL("clicked()"), \
            self.deleteModuleButtonClicked)
        self.connect(self.ui.specialModulesList, \
            SIGNAL("itemClicked(QListWidgetItem*)"), \
            self.specialModulesListClicked)
        self.connect(self.ui.commandEdit, \
            SIGNAL("textChanged()"), \
            self.moduleCommandTextChanged)
        self.connect(self.ui.moduleList, \
            SIGNAL("itemClicked(QTreeWidgetItem*, int)"), \
            self.moduleListItemClicked)
        self.connect(self.ui.nameEdit, \
            SIGNAL("textChanged(const QString&)"),
            self.nameEditTextChanged)
        self.connect(self.ui.descriptionEdit, \
            SIGNAL("textChanged(const QString&)"),
            self.descriptionEditTextChanged)
        self.connect(self.ui.dependencyEdit, \
            SIGNAL("textChanged(const QString&)"),
            self.dependencyEditTextChanged)

        self.contextName = "None"
        self.updateCurrentContextName()

        self.ui.specialModulesList.addItem(QString("For"))
        self.ui.specialModulesList.addItem(QString("If"))

        self.parameters = []
        self.context_parameters = []

    def nameEditTextChanged(self, qstring):
        """
        Called when the user is editing the name of a module.
        """
        # TODO: Check that this doesn't have the same name as another module
        self.ui.moduleList.currentItem().add_name(self.ui.nameEdit.text())
        self.ui.moduleList.currentItem().updateUi()

    def descriptionEditTextChanged(self, qstring):
        """
        Called when the user is editing the description of a module.
        """
        self.ui.moduleList.currentItem().add_description( \
            self.ui.descriptionEdit.text())
        self.ui.moduleList.currentItem().updateUi()

    def dependencyEditTextChanged(self, qstring):
        """
        Called when the user is editing the name of a module.
        """
        if str(qstring) == "":
            return
        dependencies = None
        try:
            dependencies = list(eval(str(qstring)))
        except NameError:
            # The string contains text
            return
        except SyntaxError:
            # The string is empty
            return
        except TypeError:
            # It has decimals or longs
            return
        
        error = False
        if dependencies:
            if type(dependencies) is IntType:
                dependencies = [dependencies]

            for dependency in dependencies:
                if type(dependency) is not IntType:
                    # It still contains "None" or some text
                    error = True
            
            if not error:
                self.ui.moduleList.currentItem().set_dependencies(dependencies)
                self.ui.moduleList.currentItem().updateUi()
        
#        self.ui.treeWidget.currentItem().setData(4, Qt.DisplayRole, \
 #           self.ui.dependencyEdit.text())


    def moduleListItemClicked(self, item, columnNo):
        """
        Called when a module is clicked. Populates the text entry boxes with
        module information so that it can be easily edited.
        """
        self.ui.nameEdit.setText(item.data(1, Qt.DisplayRole).toString())
        self.ui.commandEdit.setText(item.data(2, Qt.DisplayRole).toString())
        self.ui.descriptionEdit.setText(item.data(3, Qt.DisplayRole).toString())
        self.ui.dependencyEdit.setText(item.data(4, Qt.DisplayRole).toString())

    def specialModulesListClicked(self, item):
        """
        Inserts a special module (For or If) into the project.
        """
        newitem = QTreeWidgetItem()
        # TODO: Fix IDs from special modules
        newitem.setData(0, Qt.DisplayRole, QString("1"))
        newitem.setData(1, Qt.DisplayRole, QString("For"))
        newitem.setData(2, Qt.DisplayRole, QString(""))
        newitem.setData(3, Qt.DisplayRole, QString("Applies a range of parameters to a list of functions"))
        newitem.setData(4, Qt.DisplayRole, QString("None"))
        self.ui.moduleList.addTopLevelItem(newitem)

    def updateCurrentContextName(self):
        self.ui.currentContextName.setText(QString(self.contextName))

    def moduleCommandTextChanged(self):
        """
        Called when the user changes a command.
        Should check if the user has made a change to a module and should update
        the internal representation of that module to reflect it.
        """
        # Set the text of the module to contain the text of the command edit
        self.ui.moduleList.currentItem().add_command( \
            str(self.ui.commandEdit.toPlainText()))
        
        self.ui.moduleList.currentItem().updateUi()

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

        modules = self.ui.moduleList.findItems("*", Qt.MatchWildcard)
        processes = []

        # Loop through the modules, check if they are special modules
        # and if they are, make sure they have the correct parameters
        # E.g. IF modules should have a condition.
        # Also check if the command exists before trying to execute it
        for module in modules:
            # TODO: Check criteria for FOR and IF modules
            if module.command == "":
                if self.okToContinue("Warning", "The module named " + \
                        module.name + " has no command. Continue?"):

                    pass
                else:
                    return

            command = module.command
            for param in module.parameters:
                command = replace(command, param.param_id, param.value)

            executable = command.split(" ")
            if self.which(executable[0]) == None:
                # Can't find the command in the PATH
                reply = QMessageBox.question(self, "Error", \
                    "The command " + executable[0] + " does not appear " + \
                    "to exist on the PATH.",
                    QMessageBox.Cancel)

                return

            module.command = command

            process = Process(command, module.id)
            process.dependant_process_ids = module.dependencies
            processes.append(process)

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
            modules, parameters = self.parseXML(xml)

            for module in modules:

                ui = ModuleListWidgetItem(module,parent = self.ui.contextModuleList)
                self.ui.contextModuleList.addItem(ui)

            self.context_parameters = parameters
            #self.updateMappings()

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
        modules = [self.ui.contextModuleList.item(x).module for x in xrange(0, \
            self.ui.contextModuleList.count())]
        from xml.dom.minidom import Document
        doc = Document()
        list = doc.createElement("moduleList")
        doc.appendChild(list)
        for module in modules:
            mod = doc.createElement("module")
            mod.setAttribute("name", module.name)
            mod.setAttribute("id", module.id)
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

        modules = self.ui.moduleList.findItems("*", Qt.MatchWildcard)

        from xml.dom.minidom import Document
        doc = Document()
        list = doc.createElement("moduleList")
        doc.appendChild(list)

        def parseModule(module):
            print "Processing " + module.name
            mod = doc.createElement("module")
            mod.setAttribute("name", module.name)
            mod.setAttribute("id", module.id)
            description = doc.createElement("description")

#            print type(module.command + module.command + module.name)
            descriptiontext = doc.createTextNode(str(module.description))
            description.appendChild(descriptiontext)

            command = doc.createElement("command")

            commandtext = doc.createTextNode(module.command)
            command.appendChild(commandtext)

            mod.appendChild(description)
            mod.appendChild(command)

            return mod

           
            for dependency in module.dependencies:
                dep = doc.createElement("dependency")
                deptext = doc.createTextNode(str(dependency))
                dep.appendChild(deptext)
                mod.appendChild(dep)

            return mod



        for module in modules:
            print module.name
            if module.childCount() == 0:
                mod = parseModule(module)
                list.appendChild(mod)
            else:
                mod = parseModule(module)
                childnode = doc.createElement("child")
                child = parseModule(module.child(0))
                childnode.appendChild(child)
                mod.appendChild(childnode)
                #mod.appendChild(child)
                list.appendChild(mod)
            # If it's not a FOR or IF special module

        par = doc.createElement("parameters")

        for param in self.parameters:
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

            par.appendChild(parameter)

        list.appendChild(par)

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
        # TODO: Clear this first
        try:
            input = open(fileName)
            xml = input.read()
            modules, parameters = self.parseXML(xml)

            for module in modules:
                # Add the module to the list
                item = ModuleWidgetItem(module)
                item.updateUi()
                if module.children:
                    child = ModuleWidgetItem(module.children)
                    child.updateUi()
                    item.addChild(child)
                self.ui.moduleList.addTopLevelItem(item)

            # Add the parameters to the global parameter list
            self.parameters = parameters
            print "Found " + str(len(self.parameters)) + "params"
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

    def closeProject(self):
        """
        Close the current project
        """
        if self.changed:
            result = self.okToContinue("Error.", \
                "There are unsaved changes. Save them?")
            if result:
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
    
    def deleteModuleButtonClicked(self):
        """
        Delete the currently selected module from the project. Ensure that no
        other modules are using it's variables before deleting them
        """
        

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
        self.ui.contextModuleList.addItem(ModuleListWidgetItem(module))
        self.updateMappings()

    def updateMappings(self):
        """
        Repopulates the table of symbol -> description + mapping and is called
        whenever a change is made to the modules
        """
        self.ui.mappingsTable.setSortingEnabled(False)
        self.ui.mappingsTable.setRowCount(len(self.parameters))

        counter = 0
        for param in self.parameters:
            print "adding"
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
        # Check if the module being loaded redefines any current parameter, and
        # if it is, rename the parameter and edit the command for the module
        # that uses it.

        # Construct the new module
        newitem = ModuleWidgetItem(item.module)
        
        highestId = 0
        duplicateNameCount = 0

#        modules = [self.ui.contextModuleList.item(x).module for x in xrange(0, \
 #           self.ui.contextModuleList.count())]
 
        modules = self.ui.moduleList.findItems("*", Qt.MatchWildcard)

        for module in modules:
            # Check if any current modules have a higher ID
            if module.id > highestId:
                highestId = int(module.id)
        
        # Check for the parameters of the module redefining any parameters
        # Loop through the parameters that are used in the context module
        command = newitem.command
        
        # Strip out any words that don't begin with %
        commands = command.split(" ")

        for variable in commands:
            if not str(variable).startswith("%"):
                commands.remove(variable)

        # Commands now contains all of the parameters used in the module command
        # Loop through the context_params list and get the corresponding parameter
        # objects
        parameterObjects = []

        for newcommand in commands:
            for param in self.context_parameters:
                if param.param_id == newcommand:
                    parameterObjects.append(deepcopy(param))
                
        # Now that we have all the parameter objects relating to this module,
        # we need to check if they have been used before or not

        # Loop through all existing parameters and check if any of the commands
        # have been redefined.
        numDuplicates = 0
        for parameterObject in parameterObjects:
             
            # Check if this module redefines this parameter
            pattern = re.compile(parameterObject.param_id + "[0-9]*")
            print parameterObject.param_id + "[0-9]*"


            for existingParameter in self.parameters:
                print "checking" + existingParameter.param_id
                if pattern.match(existingParameter.param_id):
                    print "duplicate found"
                    numDuplicates += 1
        
            # If there were duplicates, rename this command and edit the module
            if numDuplicates > 0:
                newName = str(parameterObject.param_id) + str(numDuplicates)
                print "newName is " + newName
                print "old command is " + newitem.command
                newitem.command = newitem.command.replace(str(parameterObject.param_id), str(newName))

                print "new command is " + newitem.command
                parameterObject.param_id = newName

            numDuplicates = 0

            # Add the parameter to the global parameter list
            try:
                self.parameters.index(parameterObject)
            except ValueError:
                # The parameter doesn't exist in the global parameter
                # list so add it.
                self.parameters.append(parameterObject)
        
        # Check for module name conflicts
        pattern = re.compile(newitem.name + "( \([0-9]+\))?")
        duplicateNameCount = 0
        for module in modules:
            print "matching " + module.name + " against " + newitem.name
            if pattern.match(module.name):
                print "match"
                # If a copy of this module already exists then we add (n) onto
                # the name of this module, where n is the number of modules of
                # that type that already exist
                duplicateNameCount += 1

        if duplicateNameCount > 0:
            newitem.name = newitem.name + " (" + str(duplicateNameCount) + ")"

        self.changed = True

        highestId += 1

        newitem.add_id(highestId)
        
        newitem.updateUi()

        self.ui.moduleList.addTopLevelItem(newitem)

        self.updateMappings()

    # the following function is from
    # http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
    def which(self, program):
        """
        Search the os PATH variable to see if a script / program exists and that
        it is executable
        """
        import os
        def is_exe(fpath):
            return os.path.exists(fpath) and os.access(fpath, os.X_OK)

        fpath, fname = os.path.split(program)
        if fpath:
            if is_exe(program):
                return program
        else:
            for path in os.environ["PATH"].split(os.pathsep):
                exe_file = os.path.join(path, program)
                if is_exe(exe_file):
                    return exe_file

        return None

