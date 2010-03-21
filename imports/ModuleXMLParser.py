from xml.parsers import expat

class Parameter():
	def __init__(self):
		self.id = ""
		self.description = ""
		self.value = ""

	def addId(self, id):
		self.id = id
		
	def addDescription(self, desc):
		self.desc = desc
		
	def addValue(self, value):
		self.value = value

class Module():
	
	def __init__(self, name):
		self.name = name
		self.command = ""
		self.parameters = []
		self.description = ""

	def addParameter(self, param):
		self.parameters.append(param)

class ModuleXMLParser:
	def __init__(self):
		# 3 handler functions
		self.currentModule = None
		self.currentParam = None

		self.currentItem = ""

		self.currentDescription = ""
		self.currentValue = ""
		self.currentCommand = ""

		self.inDescription = False
		self.inCommand = False
		self.inValue = False

		self.stack = []

	def start_element(self, name, attrs):
		print "Start Element", name
		if name == "module":
			self.stack.append(name)
			print 'Start element:', name, attrs
			self.currentModule = Module(attrs['name'])
		elif name == "param":
			self.stack.append(name)
			self.currentParam = Parameter()
		elif name == "description":
			if self.stack[-1] == "module":
				self.inDescription = True
		elif name == "value":
			self.inValue = True
		elif name == "command":
			self.inCommand = True

		print self.stack

	def end_element(self, name):
		if name == "module":
			self.stack.pop()
			#self.currentModule = None
		elif name == "description":
			self.inDescription = False
			self.currentModule.description = self.currentDescription
			self.currentDescription = ""
		elif name == "param":
			self.stack.pop()
			self.currentModule.addParameter(self.currentParam)
			self.currentParam = None
		elif name == "value":
			self.currentParam.addValue(self.currentValue)
			self.currentValue = ""
			self.inValue = False
		elif name == "command":
			self.currentModule.command = self.currentCommand
			self.currentCommand = ""
			self.inCommand = False
			
		print self.stack

	def char_data(self, data):
		data = data.strip()
		if data:
			if self.inDescription:
				self.currentDescription = self.currentDescription + data
			elif self.inCommand:
				self.currentCommand = self.currentCommand + data
			elif self.inValue:
				self.currentValue = self.currentValue + data
				print self.currentValue

	def parse(self, text):

		parser = expat.ParserCreate()

		parser.StartElementHandler = self.start_element
		parser.EndElementHandler = self.end_element
		parser.CharacterDataHandler = self.char_data
		parser.Parse(text, 1)
		return self.currentModule

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
		print "	Parameter found.", param.value, "s"
#		print "		" , param.id. param.description, param.value

