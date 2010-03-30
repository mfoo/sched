class Process:
    """
    This class represents a single process that can be represented in the
    pipeline.
    """
    def __init__(self, command, prefix = None, runnable = True):
        self.dependantProcessIDs = []
        self.process = None
        self.numRemaining = 0
        self.prefix = prefix
        self.command = command
        self.runnable = runnable
        self.runnable = True
        
    def addDependant(self, process):
        self.numRemaining += 1
        self.dependantProcessIDs.append(process)
