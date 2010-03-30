"""
Class represents a parameter for a specific module, containing an id, a
description and a mapping to a value.
"""

class Parameter():
    """
    Class represents a parameter for a specific module, containing an id, a
    description and a mapping to a value.
    """
    def __init__(self):
        self.param_id = ""
        self.description = ""
        self.value = ""

    def add_id(self, param_id):
        """
        Add an ID to the parameter. Used in the XML parser.
        """
        self.param_id = param_id
        
    def add_description(self, desc):
        """
        Add a description to the parameter. Used in the XML parser.
        """
        self.description = desc
        
    def add_value(self, value):
        """
        Add a mapping to the parameter. Used in the XML parser.
        """
        self.value = value
