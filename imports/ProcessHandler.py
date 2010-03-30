"""
Created on 2 Feb 2010

@author: Martin Foot
"""

import sys
import signal
import subprocess
import process
import time
import os
import re
from forms.JobProcessingWindow import JobProcessingWindow
from threading import Thread
from PyQt4.QtCore import QTimer
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ProcessHandler:
    """
    This class is used to store and edit lists of processes and handle the 
    execution of the process.
    """
    def __init__(self, ready = []):
        self.running = []
        self.waiting = []
        self.outputBuffer = []
        self.ui = JobProcessingWindow()
        self.value = 0

        for process in ready:
            self.addProcess(process)

#        # Set the handler function as the handler for child process ending signals
#        signal.signal(signal.SIGCHLD, self.handler)

        # Set the signal handler to restart system calls that are interrupted
        signal.siginterrupt(signal.SIGCHLD, False)
        
    def start(self):
        self.ui.ui.progressBar.setMinimum(0)
        self.ui.ui.progressBar.setMaximum(len(self.waiting))
        self.ui.ui.progressBar.setValue(0)
        self.ui.ui.logText.appendPlainText("Starting")

        self.startTime = time.time()
        print len(self.waiting)
        for process in self.waiting:
#            print len(self.running)
            print "checking"
            print len(self.running)
            if(len(self.running) < 4):
                if process.runnable:
                    print "added running"
                    self.running.append(self.waiting.pop(self.waiting.index(process)))
                    self.execute(process)
#            else:
#                print "tooo mnany"
#                print len(self.running)
#                break

        self.timer = QTimer()
        self.ui.connect(self.timer, SIGNAL("timeout()"), self.updateProgressBar)
        self.timer.start(250)

    def updateProgressBar(self):
        self.handler()
        self.ui.ui.progressBar.setValue(self.value)
        for item in self.outputBuffer:
            self.ui.ui.logText.appendPlainText(item)
            self.outputBuffer.remove(item)

    def addProcess(self, process):
        print "Adding process. %s" % (process.command,)
        # If there are no processes running and the length of the focus process list is zero
        self.waiting.append(process)

    def execute(self, process):
        """
        Execute the specified process
        """
        print "Executing process %s" % (process.command,)
        self.outputBuffer.append("Executing process %s" % (process.command,))
        process.process = subprocess.Popen([process.command], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

#    def handler(self, sig, frame):
    def handler(self):
     #   print "Handler triggered"
      #  # Find which process has ended
#        self.ui.ui.logText.appendPlainText("Process has finished. There are %d running, %d waiting processes left. Current duration: %d\n" % (len(self.running), len(self.waiting), (time.time() - self.startTime)))
#        print "Process has finished. There are %d running, %d waiting processes left. Current duration: %d" % (len(self.running), len(self.waiting), (time.time() - self.startTime))
        for process in self.running:
            if process.process:
                if process.process.poll() == 0 or process.process.poll() == 1:
                # This process has ended or failed
                    print "Found the process that has ended, removing it."
                    self.value += 1
                       
                    # TODO: Stop the QTimer if finished
                    self.running.remove(process)

                    if(len(self.waiting) != 0):
                        for executableProcess in self.waiting:
    #                        executableProcess = self.waiting[:1][0]
                            if executableProcess.runnable:
                                self.waiting.remove(executableProcess)
                                self.running.append(executableProcess)
                                self.execute(executableProcess)
                                break
                    self.outputBuffer.append("Process has finished. There are %d running, %d waiting processes left. Current duration: %d\n" % (len(self.running), len(self.waiting), (time.time() - self.startTime)))

                                
        
#        for process in self.waiting:
#            print "    %s"% (process.command,)
        
# Set the movement parameters 
# function chunks from http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python 
# This function splits a list into smaller lists of size l
def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


#handler = ProcessHandler()
#import pprint

if __name__ == "__main__":

    # TODO: 
    startTime = time.time()


# Make a list of all files to manage
    files = [x for x in xrange(1144, 1156)]
    rows = list(chunks(files, 12))
    amount = 1
    for row in rows:
	if amount < 20000:
		mask = 1
		stage = 1
		while len(row) > 0:
			newrow = []
			# Loop through every other element in the list except the last one if there's an odd number
			for file in [x for x in row[::2] if (row.index(x) + 1) != len(row)]:
				newrow.append(file)
				print "Processing:"
				pprint.pprint(row)
				if len(row) == 12:
					stackProcess = process.Process("convert stacked%d.tiff  -extent 4230x2050 stacked%d.tiff mask%d.png -gravity East -composite out%d.png" % (file, file + 1, mask, file), "merge process")
	
				elif len(row) == 6:
					stackProcess = process.Process("convert out%d.png  -extent 7794x2050 out%d.png mask%d.png -gravity East -composite outa%d.png" % (file, file + 2, mask, file), "merge process 2")
	
	                        elif len(row) == 3:
					stackProcess = process.Process("convert outa%d.png  -extent 14922x2050 outa%d.png mask%d.png -gravity East -composite outb%d.png" % (file, file + 4, mask, file), "merge process 3")
					newrow.append(row[-1])

#				elif len(row) == 2:

				elif len(row) == 2:
					stackProcess = process.Process("convert outb%d.png  -extent 22050x2050 outa%d.png mask%d.png -gravity East -composite outc%d.png" % (file, file + 8, mask, file), "merge process 4")
					#handler.addFocus(stackProcess)	
				handler.addFocus(stackProcess)
				
			mask += 1
		#	if len([x for x in row[::2] if (row.index(x) + 1) != len(row)]) % 2 != 0:
		#		newrow.append(row[-1])
	#		if len(newrow) == 0:
	#			newrow.append(row[-1])
			row = newrow
			print "Next row to process:"		
			pprint.pprint(row)
	
			while not len(handler.running) == 0:
				print "Waiting for row %d stage %d." % (amount, stage)
				time.sleep(10)
	
			stage += 1
	
		amount += 1
	




    while not len(handler.running) == 0:
        print "There are %i ready lv 2 combo processes, and %i running processes left." % (len(handler.waiting), len(handler.running))
        time.sleep(60)



# Start at a number with two columns to stop problems later
# TODO; This is going to break if there are more than 89 stacks, perhaps use chars?

