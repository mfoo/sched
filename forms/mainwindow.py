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

import os
import re

from forms.ui_mainwindow import Ui_MainWindow
from forms.modulelistwidget import ModuleListWidgetItem

from imports import Module, Parameter
from imports.modulewidgetitem import ModuleWidgetItem

class DraggableListWidget(QListWidget):
    def __init__(self, parent=None):
        self.test = None
        QListWidget.__init__(self, parent)
        self.dropEvent = self.newDropEvent
        self.setGeometry(QRect(10, 30, 131, 271))
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setObjectName("listWidget")

#    def dragEnterEvent(self, event):
#        self.test = event.source()
#        print "dragenterevnt"
#        print self.test.name

    def newDropEvent(self, event):
        print "lolevent"
        dragItem = self.currentItem()
        print str(dragItem.nameLabel.text())
        QListWidget.dropEvent(self, event)
        dragItem.generateWidget(dragItem.module.name, \
            dragItem.module.description)
        dragItem.widget.parent = dragItem
        dragItem.layout.addWidget(QLabel(QString(dragItem.module.name)))
#        self.setItemWidget(dragItem, dragItem.widget)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.listWidget = DraggableListWidget(self.ui.centralWidget)
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
        self.connect(self.ui.specialModulesList, \
            SIGNAL("itemClicked(QListWidgetItem*)"), \
            self.specialModulesListClicked)
        self.connect(self.ui.commandEdit, \
            SIGNAL("textChanged()"), \
            self.moduleCommandTextChanged)
        self.connect(self.ui.treeWidget, \
            SIGNAL("itemClicked(QTreeWidgetItem*, int)"), \
            self.treeWidgetItemClicked)
        self.connect(self.ui.nameEdit, \
            SIGNAL("textChanged(const QString&)"),
            self.nameEditTextChanged)
        self.connect(self.ui.descriptionEdit, \
            SIGNAL("textChanged(const QString&)"),
            self.descriptionEditTextChanged)
        self.connect(self.ui.dependencyEdit, \
            SIGNAL("textChanged(const QString&)"),
            self.dependencyEditTextChanged)

        # Configure the column headings for the variable mappings table
        headers = ["Symbol", "Description", "Mapping"]
        self.ui.mappingsTable.setColumnCount(len(headers))
        self.ui.mappingsTable.setHorizontalHeaderLabels(headers)

        self.ui.listWidget.setAcceptDrops(True)
        self.ui.listWidget.setDragEnabled(True)
        self.ui.listWidget.setDragDropMode(QAbstractItemView.InternalMove)

        # Set up the header for the module list
        treeWidgetHeaderList = QStringList()
        treeWidgetHeaderList.append("ID")
        treeWidgetHeaderList.append("Name")
        treeWidgetHeaderList.append("Command")
        treeWidgetHeaderList.append("Description")
        treeWidgetHeaderList.append("Dependencies")

        self.ui.treeWidget.setHeaderLabels(treeWidgetHeaderList)
        self.contextName = "None"
        self.updateCurrentContextName()

        self.ui.specialModulesList.addItem(QString("For"))
        self.ui.specialModulesList.addItem(QString("If"))

    def nameEditTextChanged(self, qstring):
        """
        Called when the user is editing the name of a module.
        """
        # TODO: Check that this doesn't have the same name as another module
        self.ui.treeWidget.currentItem().add_name(self.ui.nameEdit.text())
        self.ui.treeWidget.currentItem().updateUi()

    def descriptionEditTextChanged(self, qstring):
        """
        Called when the user is editing the description of a module.
        """
        self.ui.treeWidget.currentItem().add_description( \
            self.ui.descriptionEdit.text())
        self.ui.treeWidget.currentItem().updateUi()


    def dependencyEditTextChanged(self, qstring):
        """
        Called when the user is editing the name of a module.
        """
        # TODO: Implement dependencies
        pass
#        self.ui.treeWidget.currentItem().setData(4, Qt.DisplayRole, \
 #           self.ui.dependencyEdit.text())


    def treeWidgetItemClicked(self, item, columnNo):
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
        newitem.setData(0, Qt.DisplayRole, 1)
        newitem.setData(1, Qt.DisplayRole, QString("For"))
        newitem.setData(2, Qt.DisplayRole, QString(""))
        newitem.setData(3, Qt.DisplayRole, QString("Applies a range of parameters to a list of functions"))
        newitem.setData(4, Qt.DisplayRole, QString("None"))
        self.ui.treeWidget.addTopLevelItem(newitem)

    def updateCurrentContextName(self):
        self.ui.currentContextName.setText(QString(self.contextName))

    def moduleCommandTextChanged(self):
        """
        Called when the user changes a command.
        Should check if the user has made a change to a module and should update
        the internal representation of that module to reflect it.
        """
        # Set the text of the module to contain the text of the command edit
        self.ui.treeWidget.currentItem().add_command( \
            str(self.ui.commandEdit.toPlainText()))
        
        self.ui.treeWidget.currentItem().updateUi()

#        currentModule = self.ui.treeWidget.currentItem()
#        currentModule.module.command = text
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

        modules = self.ui.treeWidget.findItems("*", Qt.MatchWildcard)
        processes = []

        # Loop through the modules, check if they are special modules
        # and if they are, make sure they have the correct parameters
        # E.g. IF modules should have a condition.
        # Also check if the command exists before trying to execute it
        for module in modules:
            # TODO: Mark a module as existing if it has been found so not all of
            # them need to be checked?
            # TODO: Take into account "nice" commands
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

        for module in modules:
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

            for module in modules:
                ui = ModuleListWidgetItem(module,parent = self.ui.listWidget)
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
        

        modules = self.ui.treeWidget.findItems("*", Qt.MatchWildcard)

        from xml.dom.minidom import Document
        doc = Document()
        list = doc.createElement("moduleList")
        doc.appendChild(list)

        def parseModule(module):
            print "Processing " + module.name
            mod = doc.createElement("module")
            mod.setAttribute("name", module.name)
            description = doc.createElement("description")

#            print type(module.command + module.command + module.name)
            descriptiontext = doc.createTextNode(str(module.description))
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
            modules = self.parseXML(xml)

            for module in modules:
                # Add the module to the list
                item = ModuleWidgetItem(module)
                item.updateUi()
                if module.children:
                    child = ModuleWidgetItem(module.children)
                    child.updateUi()
                    item.addChild(child)
                self.ui.treeWidget.addTopLevelItem(item)
                
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
        self.ui.listWidget.addItem(ModuleListWidgetItem(module))
        self.updateMappings()

    def updateMappings(self):
        """
        Repopulates the table of symbol -> description + mapping and is called
        whenever a change is made to the modules
        """
#        modules = self.ui.treeWidget.items(itemType)
        self.ui.mappingsTable.setSortingEnabled(False)
        modules = self.ui.treeWidget.findItems("*", Qt.MatchWildcard)
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




 #       self.ui.treeWidget.addTopLevelItem(QTreeWidgetItem(["lol"]))
  #      self.ui.treeWidget.addTopLevelItem(QTreeWidgetItem(["lott"]))
   #     self.ui.treeWidget.itemAt(0,0).addChild(QTreeWidgetItem(["ahah"])) 

        # Get the ID from the module
        newitem = ModuleWidgetItem(item.module)
        #newItem.setModule(item.module)
        newitem.updateUi()
#        id += 1
        self.ui.treeWidget.addTopLevelItem(newitem)

        modules = self.ui.treeWidget.findItems("*", Qt.MatchWildcard)

        for module in modules:
            for parameter in module.parameters:
                for newParameter in newitem.parameters:
                    if parameter == newParameter:
                        # TODO: Add the name of the module to the param name?
                        # Use a number?
                        print "temp"
            if module.name == newitem.name:
                # If a copy of this module already exists then we add (n) onto
                # the name of this module, where n is the number of modules of
                # that type that already exist
                try:
                    item.module.count += 1
                except AttributeError:
                    item.module.count = 1

        self.changed = True
#        newmodule = deepcopy(item).module
        
#        try:
#            newmodule.name = newmodule.name + " (" + str(newmodule.count) + ")"
#        except AttributeError:
#            pass

 #       self.ui.projectModuleList.addItem(ModuleListWidgetItem(newmodule, \
#            parent=self.ui.projectModuleList))
        self.updateMappings()

    # the following function is from
    # http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
    def which(self, program):
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

