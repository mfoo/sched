from xml.parsers import expat
from Parameter import Parameter
from Module import Module

class ModuleXMLParser:
	def __init__(self):
		self.moduleList = []

		self.currentModule = None
		self.currentParam = None
		self.cdata = ""

		self.inDescription = False
		self.inCommand = False
		self.inValue = False
		self.inId = False

	def start_element(self, name, attrs):
		if name == "module":
			self.currentModule = Module(attrs['name'])
		elif name == "param":
			self.currentParam = Parameter()
		elif name == "description":
			self.inDescription = True
		elif name == "value":
			self.inValue = True
		elif name == "command":
			self.inCommand = True
		elif name == "id":
			self.inId = True


	def end_element(self, name):
		if name == "description":
			self.inDescription = False
			if self.currentParam:
				# Parser is inside a parameter, add the description to it
				self.currentParam.addDescription(self.cdata)
			else:
				self.currentModule.addDescription(self.cdata)

			self.cdata = ""
		elif name == "value":
			self.inValue = False
			self.currentParam.addValue(self.cdata)
			self.cdata = ""
		elif name == "command":
			self.inCommand = False
			self.currentModule.addCommand(self.cdata)
			self.cdata = ""
		elif name == "id":
			self.inId = False	
			self.currentParam.addId(self.cdata)
			self.cdata = ""
		elif name == "param":
			self.currentModule.addParameter(self.currentParam)
			self.currentParam = None
		elif name == "module":
			self.moduleList.append(self.currentModule)
			

	def char_data(self, data):
		data = data.strip()
		if data:
			if self.inDescription or self.inId or self.inCommand or self.inValue:
				self.cdata = self.cdata + data

	def parse(self, text):

		parser = expat.ParserCreate()

		parser.StartElementHandler = self.start_element
		parser.EndElementHandler = self.end_element
		parser.CharacterDataHandler = self.char_data
		parser.Parse(text, 1)

		return self.moduleList

if __name__ == "__main__":
	parser = ModuleXMLParser()

	input = """<?xml version="1.0" encoding="UTF-8"?>
<moduleList xmlns:xsi="http://w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="sched.xsd">
	<module name="hello">
		<description>a module</description>
		<command>cp %0 %1</command>
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
	</module>
</moduleList>"""

	mod = parser.parse(input)	
	for param in mod.parameters:
		print "Parameter found. " , param.id, param.description, param.value

