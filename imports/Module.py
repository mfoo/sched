"""
Class represents a module in a project, containing a command and a list of
parameters as well as a name and description.
"""

class Module():
    """
    Class represents a module in a project, containing a command and a list of
    parameters as well as a name and description.
    """
    # TODO: Remove this
    def __init__(self, *args):
        if len(args) == 0:
            # No name was supplied
            self.name = ""
        else:
            self.name = args[0]

        self.command = ""
        self.parameters = []
        self.description = ""
        self.children = None

    def add_name(self, name):
        """
        Add a name to the module
        """
        self.name = name

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
