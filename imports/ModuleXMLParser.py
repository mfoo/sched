"""
Module containing the ModuleXMLParser class
"""

from xml.parsers import expat
from Parameter import Parameter
from Module import Module

class ModuleXMLParser:
    """
    ModuleXMLParser will parse a list of modules and returns it.
    """
    def __init__(self):
        self.module_list = []
        self.param_list = []

        self.current_module = None
        self.current_param = None
        self.cdata = ""
        self.parent = None

        self.in_description = False
        self.in_command = False
        self.in_value = False
        self.in_id = False
        self.in_child = False
        self.in_dependency = False

    def start_element(self, name, attrs):
        """
        Function called when the start of an XML element is found
        """
        if name == "module":
            self.current_module = Module(attrs['name'])
            self.current_module.add_id(attrs['id'])
        elif name == "dependency":
            self.in_dependency = True
        elif name == "param":
            self.current_param = Parameter()
        elif name == "description":
            self.in_description = True
        elif name == "value":
            self.in_value = True
        elif name == "command":
            self.in_command = True
        elif name == "id":
            self.in_id = True
        elif name == "child":
            self.in_child = True
            self.parent = self.current_module

    def end_element(self, name):
        """
        Function called when the end of an XML element is found
        """
        if name == "description":
            self.in_description = False
            if self.current_param:
                # Parser is inside a parameter, add the description to it
                self.current_param.add_description(self.cdata)
            else:
                self.current_module.add_description(self.cdata)

            self.cdata = ""
        elif name == "dependency":
            self.current_module.dependencies.append(int(self.cdata))
            self.in_dependency = False
            self.cdata = ""
        elif name == "value":
            self.in_value = False
            self.current_param.add_value(self.cdata)
            self.cdata = ""
        elif name == "command":
            self.in_command = False
            self.current_module.add_command(self.cdata)
            self.cdata = ""
        elif name == "id":
            self.in_id = False    
            self.current_param.add_id(self.cdata)
            self.cdata = ""
        elif name == "param":
            self.param_list.append(self.current_param)
            self.current_param = None
        elif name == "module":
            self.module_list.append(self.current_module)
        elif name == "child":
            # TODO: Allow having more than one child
            self.parent.children = self.current_module
            self.current_module = self.parent
            self.in_child = False
            
    def char_data(self, data):
        """
        Function called when some character data within an XML element is found
        """
        data = data.strip()
        if data:
            if self.in_description or self.in_id or self.in_command or self.in_value or self.in_dependency:
                self.cdata = self.cdata + data

    def parse(self, text):
        """
        Sets up expat with the correct custom parser functions and parses text
        """
        parser = expat.ParserCreate()

        parser.StartElementHandler = self.start_element
        parser.EndElementHandler = self.end_element
        parser.CharacterDataHandler = self.char_data
        parser.Parse(text, 1)

        return self.module_list

if __name__ == "__main__":
    _PARSER = ModuleXMLParser()

    _INPUT = """<?xml version="1.0" encoding="UTF-8"?>
<moduleList xmlns:xsi="http://w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="sched.xsd">
    <parameters>
        <param>
            <id>0</id>
            <description>The name of the file to copy</description>
            <value>source</value>
        </param>
        <param>
            <id>1</id>
            <description>The new name of the file</description>
            <value>destination</value>
        </param>
    </parameters>
    <module name="hello">
        <child>
            <module name="lol">       
                <description>a module</description>
                <command>cp %0 %1</command>
            </module>
        </child>       
        <description>a module</description>
        <command>cp %0 %1</command>
    </module>
</moduleList>"""

    _MOD = _PARSER.parse(_INPUT)   
    
    for module in _MOD:
        if module.children:
            print "Found child!" + module.children.name

        for _param in module.parameters:
            print "Parameter found. " , _param.description, _param.value

