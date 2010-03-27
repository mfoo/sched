class Process:
    """
    This class represents a single process that can be represented in the
    pipeline.
    """
    def __init__(self, command, prefix, runnable = True):
        self.dependantProcessIDs = []
        self.numRemaining = 0
        self.prefix = prefix
        self.command = command
        self.runnable = runnable
        self.process = None
        #print "Process being created with command: %s" % (command,)
        # File handles for input / output? Not needed yet.
        # (Also, next process, I.E process to pipe my OUT into their IN
        
    def addDependant(self, process):
        self.numRemaining += 1
        self.dependantProcessIDs.append(process)
        #print "Process %s has had dependant added: %s" % (self.prefix, process.prefix)
        
    def setProcess(self, process):
        self.process = process
