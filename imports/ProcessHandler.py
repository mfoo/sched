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

startTime = time.time()

class ProcessHandler:
    """
    This class is used to store and edit lists of processes and handle the 
    execution of the processs.
    """
    def __init__(self):
        self.blocked = []
        self.running = []
        self.readyExposure = []
        #self.finishedProcesses = []
        self.readyFocus = []
        
        # Set the handler function as the handler for child process ending signals
        signal.signal(signal.SIGCHLD, self.handler)
        
        # Set the signal handler to restart system calls that are interrupted
        signal.siginterrupt(signal.SIGCHLD, False)

    def addFocus(self, process):
        print "Adding focus process. %s" % (process.command,)
        # If there are no waiting processes for exposure fusion
        if(len(self.readyExposure) == 0):
            # If there are no processes running and the length of the focus process list is zero
            if(len(self.running) < 3) and (len(self.readyFocus) == 0):
               # Run the focus stack.
               self.execute(process)
               self.running.append(process)
               
               
            # Else there are already processes running so stick it on the end of the list
            else:
                self.readyFocus.append(process)
        # If there are still exposure processes running, add it to ready focus.
        else:
            self.readyFocus.append(process)

    def execute(self, process):
        """
        Execute the specified process
        """
        process.process = subprocess.Popen([process.command], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True);

    def handler(self, sig, frame):
        # Find which process has ended
        print "Process has finished. There are %d running, %d waiting exposure and %d waiting focus processes left. Duration: %d" % (len(self.running), len(self.readyExposure), len(self.readyFocus), (time.time() - startTime))
        for process in self.running:
            # When the camera process ends it will trigger this handler, and it has no process so ignore it.
            #if process.process != None:
            if process.process != None:
                if process.process.poll() == 0 or process.process.poll() == 1:
                # This process has ended or it failed
                    print "Found the process that has ended, removing it."
                    self.running.remove(process)

                # If there are still exposure processes waiting, execute one
                    if(len(self.readyExposure) != 0):
                        print "Running new exposure fusion process"
                        executableProcess = self.readyExposure[:1][0]
                        self.readyFocus = self.readyFocus[1:]
                        self.execute(executableProcess)
                        self.running.append(executableProcess)
                    
                # If there aren't any waiting exposure processes, check for focus processes
                    elif(len(self.readyFocus) != 0):
                        print "Running new focus stacking process."
                        executableProcess = self.readyFocus[:1][0]
                        self.readyFocus = self.readyFocus[1:]
                        self.execute(executableProcess)
                        self.running.append(executableProcess)
            else:
                print "PROCESS WAS NULL"
                print process.command          


# Set the movement parameters 
# function chunks from http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python 
# This function splits a list into smaller lists of size l
def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

handler = ProcessHandler()
#for name in xrange(1000, 1154, 2):
#	if (name - 1000) % 12 != 0 and name != 1000:
#		# They have reached the end, don't merge the next two
##for x in xrange(1000, 1085):
#		stackProcess = process.Process("convert stacked%d.tiff  -extent 4230x2050 stacked%d.tiff mask.png -gravity East -composite out%d.png" % (name, name+1, name), "merge process")
#		handler.addFocus(stackProcess)
#
## The composites have been 	
#	# Wait for the processes to have finished executing        
#while (not len(handler.blocked) == len(handler.running) == 0):
#    print "There are %i ready lv 1 combo processes, and %i running processes left." % (len(handler.readyFocus), len(handler.running))
#    time.sleep(60)

# They have all been combined with their neighbour, combine them across
#amount = 0
#for name in xrange(1002, 1150, 4):
#	if (name - 1000) % 12 != 0:
		# They have reached the end, don't merge the next two
#for x in xrange(1000, 1085):
#	if amount == 5:
#		amount = 0
#	else:
#	stackProcess = process.Process("convert out%d.png  -extent 7794x2050 out%d.png mask2.png -gravity East -composite outa%d.png" % (name, name+2, name), "merge process 2")
#handler.addFocus(stackProcess)
#	amount += 1
import pprint

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
	
			while (not len(handler.blocked) == len(handler.running) == 0):
				print "Waiting for row %d stage %d." % (amount, stage)
				time.sleep(10)
	
			stage += 1
	
		amount += 1
	




while (not len(handler.blocked) == len(handler.running) == 0):
    print "There are %i ready lv 2 combo processes, and %i running processes left." % (len(handler.readyFocus), len(handler.running))
    time.sleep(60)



# Start at a number with two columns to stop problems later
# TODO; This is going to break if there are more than 89 stacks, perhaps use chars?

