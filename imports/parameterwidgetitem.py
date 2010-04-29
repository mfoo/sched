from PyQt4.QtCore import QString

from PyQt4.QtGui import QTableWidgetItem

from imports.Parameter import Parameter

class ParameterWidgetItem(QTableWidgetItem, Parameter):
    """
    This class represents a single Parameter from a Module wrapped inside a
    UI widget giving it custom functionality beyond that of a normal 
    Parameter.
    """
    def __init__(self, parent=None):
        """
        Create a new instance with the specified parent.
        """
        QTableWidgetItem.__init__(self, parent)
        Parameter.__init__(self)

    def setParam(self, parameter):
        """
        Construct a UI widget from a given Parameter object.
        """
        self.add_id(parameter.param_id)
        self.add_description(parameter.description)
        self.add_value(parameter.value)
        self.updateUi()

    def updateUi(self):
        """
        Populate the rows in this table record with the values from the
        Parameter.
        """
        self.setData(
