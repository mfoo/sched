"""
This class represents a single process that can be represented in the
pipeline.
"""

class Process:
    """
    This class represents a single process that can be represented in the
    pipeline.
    """
    def __init__(self, command, id, prefix = None, runnable = True):
        self.dependant_process_ids = []
        self.process_id = id
        self.process = None
        self.num_remaining = 0
        self.prefix = prefix
        self.command = command
        self.runnable = runnable
        self.runnable = True
        
    def add_dependant(self, process):
        """
        Add a process that this process is dependant on. This process will not
        be executed until all dependants have been executed.
        """
        self.num_remaining += 1
        self.dependant_process_ids.append(process)
