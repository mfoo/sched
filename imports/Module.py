class Module():
	
	def __init__(self, name):
		self.name = name
		self.command = ""
		self.parameters = []
		self.description = ""

	def addDescription(self, desc):
		self.description = desc

	def addCommand(self, command):
		self.command = command

	def addParameter(self, param):
		self.parameters.append(param)
