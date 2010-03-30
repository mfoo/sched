from PyQt4.QtGui import *
from PyQt4.QtCore import *
from forms.Ui_MainWindow import Ui_MainWindow
from imports import Module, Parameter
from forms.Ui_ModuleListWidget import Ui_ModuleListWidget
import os
from string import replace

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Configure individual column widths
        self.ui.mappingsTable.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)
        self.ui.mappingsTable.horizontalHeader().setResizeMode(1, QHeaderView.Stretch)
        self.ui.mappingsTable.horizontalHeader().setResizeMode(2, QHeaderView.ResizeToContents)

        self.connect(self.ui.listWidget, SIGNAL("itemClicked(QListWidgetItem*)"), self.globalModuleListClickHandler)
        self.connect(self.ui.projectModuleList, SIGNAL("itemClicked(QListWidgetItem*)"), self.projectModuleListClickHandler)
        self.connect(self.ui.actionOpen_Project, SIGNAL("activated()"), self.openFileClicked)
        self.connect(self.ui.actionSave_Project, SIGNAL("activated()"), self.saveProjectClicked)
        self.connect(self.ui.actionExit, SIGNAL("activated()"), self.closeProject)
        self.connect(self.ui.executeButton, SIGNAL("clicked()"), self.execute)
        headers = ["Symbol", "Description", "Mapping"]
        self.ui.mappingsTable.setColumnCount(len(headers))
        self.ui.mappingsTable.setHorizontalHeaderLabels(headers)

        self.connect(self.ui.newGlobalModuleButton, SIGNAL("clicked()"), self.globalModuleButtonClicked)

        self.connect(self.ui.newProjectModuleButton, SIGNAL("clicked()"), self.projectModuleButtonClicked)

    def openFileClicked(self):
        fileName = QFileDialog.getOpenFileName(self, "Open File", os.path.expanduser("~"), "Sched files (*)")
        if fileName:
            self.loadProject(fileName)

    def execute(self):
        from imports.ProcessHandler import ProcessHandler
        from imports.process import Process
        modules = [self.ui.projectModuleList.item(x).module for x in xrange(0, self.ui.projectModuleList.count())]
        processes = []
        for module in modules:
            command = module.command
            for param in module.parameters:
                command = replace(command, param.id, param.value)
#            command = "sleep 5"
                command = "sleep 5"
            processes.append(Process(command))
            
        self.handler = ProcessHandler(processes)

        self.handler.ui.show()
       
        self.handler.start()

    def saveProjectClicked(self):
        modules = [self.ui.projectModuleList.item(x).module for x in xrange(0, self.ui.projectModuleList.count())]
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
                idtext = doc.createTextNode(param.id)
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
        print prettyxml

        fileName = QFileDialog.getSaveFileName(self, "Save File", os.path.expanduser("~"), "Sched files (*)")
        # TODO: Check if the file exists, don't overwrite it
        if fileName:
            file = open(fileName, "w")
            file.write(prettyxml)
            file.close()


    def loadProject(self, fileName):
        try:
            input = open(fileName)
            xml = input.read()
            modules = self.parseXML(xml)
            from forms.Ui_ModuleListWidget import Ui_ModuleListWidget
            for module in modules:
                ui = Ui_ModuleListWidget(module, parent = self.ui.projectModuleList)
                self.ui.projectModuleList.addItem(ui)
        except OSError:
            # TODO: Make an error message
            print "Can't load project."

    def parseXML(self, xml):
        from imports.ModuleXMLParser import ModuleXMLParser
        parser = ModuleXMLParser()
        return parser.parse(xml)

    def loadGlobals(self):
        try:
            input = open(os.path.expanduser('~') + os.sep + ".sched/modules.xml", "r")
            xml = input.read()
            modules = self.parseXML(xml)
            from forms.Ui_ModuleListWidget import Ui_ModuleListWidget
            for module in modules:
                ui = Ui_ModuleListWidget(module,parent = self.ui.listWidget)
                self.ui.listWidget.addItem(ui)

            self.updateMappings()

        except OSError:
            result = self.okToContinue("Error.", "~/.sched doesn't exist. This means that global modules cannot be saved. Created it?")
            if result:
                try:
                    os.mkdir(os.path.expanduser('~') + os.sep + ".sched")
                except OSError:
                    
                    print "Error! Can't write to the home directory."
                


    def closeProject(self):
        result = self.okToContinue("Error.", "There are unsaved changes. Save them?")
        if result:
            # TODO: Save
            print "Write this"
            #self.saveProject()
            self.close()

    def okToContinue(self, title, message):
        reply = QMessageBox.question(self, title, message, QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
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
        Shows a 'New Module' wizard that creates a local module (this project only)
        """
        self.showNewModuleWizard(True)
    

    def showNewModuleWizard(self, type):
        from forms.NewModuleWizard import NewModuleWizard
        self.newModuleWizard = NewModuleWizard(parent = self, local = type, callback = self.addNewModule)
        self.newModuleWizard.show()

    def addNewModule(self, module, local):
        print module.command
        print module.name
        print module.description
        for param in module.parameters:
            print param.id
            print param.description
            print param.value
        self.ui.listWidget.addItem(Ui_ModuleListWidget(module))
        self.updateMappings()

    def updateMappings(self):
        dataType = QMimeData()
        modules = [self.ui.projectModuleList.item(x).module for x in xrange(0, self.ui.projectModuleList.count())]
        self.ui.mappingsTable.setSortingEnabled(False)
        self.ui.mappingsTable.setRowCount(sum([len(x.parameters) for x in modules]) +1)

        counter = 0
        for module in modules:
            for param in module.parameters:
                self.ui.mappingsTable.setItem(counter, 0, QTableWidgetItem(QString(param.id)))
                self.ui.mappingsTable.setItem(counter, 1, QTableWidgetItem(QString(param.description)))
                self.ui.mappingsTable.setItem(counter, 2, QTableWidgetItem(QString(param.value)))
                counter += 1

        self.ui.mappingsTable.setSortingEnabled(True)
        
    
    def globalModuleListClickHandler(self, item):
        # Check if the module being loaded redefines any current parameter
        # TODO: If it does then rename it in the command and parameter part.
        modules = [self.ui.projectModuleList.item(x).module for x in xrange(0, self.ui.projectModuleList.count())]
        for module in modules:
            for parameter in module.parameters:
                for newParameter in item.module.parameters:
                    if parameter == newParameter:
                        # TODO: Add the name of the module to the param name? Use a number?
                        print "temp"
                        
        self.ui.projectModuleList.addItem(Ui_ModuleListWidget(item.module))
        self.updateMappings()

    def projectModuleListClickHandler(self, item):
        """
        When a module is clicked on in the current project list,
        populate the command line box with it's command.
        """
        self.ui.commandEdit.setText(QString(item.module.command))

