"""
Class represents a module in a project, containing a command and a list of
parameters as well as a name and description.
"""

class Module():
    """
    Class represents a module in a project, containing a command and a list of
    parameters as well as a name and description.
    """
    def __init__(self, name):
        self.name = name
        self.command = ""
        self.parameters = []
        self.description = ""

    def add_description(self, desc):
        """
        Add a description to the module
        """
        self.description = desc

    def add_command(self, command):
        """
        Add a command to the module
        """
        self.command = command

    def add_parameter(self, param):
        """
        Add a parameter to the module
        """
        self.parameters.append(param)
