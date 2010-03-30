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
from forms.jobprocessingwindow import JobProcessingWindow
from threading import Thread
from PyQt4.QtCore import QTimer
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from time import gmtime, strftime

class ProcessHandler:
    """
    This class is used to store and edit lists of processes and handle the 
    execution of the process.
    """
    def __init__(self, ready = []):
        self.running = []
        self.waiting = []
        self.output_buffer = []
        self.ui = JobProcessingWindow()
        self.value = 0

        for process in ready:
            self.add_process(process)
            
        # TODO: Make the Cancel button stop the self.timer
        
    def start(self):
        self.ui.ui.buttonBox.buttons()[0].setEnabled(False)
        self.ui.ui.progressBar.setMinimum(0)
        self.ui.ui.progressBar.setMaximum(len(self.waiting))
        self.ui.ui.progressBar.setValue(0)
        self.ui.ui.logText.appendPlainText("Starting")
        self.ui.ui.startTimeLabel.setText(QString(strftime("%a, %d %b %Y %H:%M:%S", gmtime())))
        
        self.startTime = time.time()
        for process in self.waiting:
            if(len(self.running) < 4):
                if process.runnable:
                    self.running.append(self.waiting.pop(self.waiting.index(process)))
                    self.execute(process)
            else:
                break

        self.timer = QTimer()
        self.ui.connect(self.timer, SIGNAL("timeout()"), self.update_progress_bar)
        self.timer.start(250)

    def update_progress_bar(self):
        self.handler()
        self.ui.ui.progressBar.setValue(self.value)
        for item in self.output_buffer:
            self.ui.ui.logText.appendPlainText(item)
            self.output_buffer.remove(item)

    def add_process(self, process):
        print "Adding process. %s" % (process.command,)
        # If there are no processes running and the length of the focus process list is zero
        self.waiting.append(process)

    def execute(self, process):
        """
        Execute the specified process
        """
        print "Executing process %s" % (process.command,)
        self.output_buffer.append("Executing process %s" % (process.command,))
        process.process = subprocess.Popen([process.command], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

    def handler(self):
        for process in self.running:
            if process.process:
                if process.process.poll() == 0 or process.process.poll() == 1:
                    # This process has ended or failed
                    print "Found the process that has ended, removing it."
                    self.value += 1

                    self.running.remove(process)

                    if(len(self.waiting) != 0):
                        for executableProcess in self.waiting:
                            if executableProcess.runnable:
                                self.waiting.remove(executableProcess)
                                self.running.append(executableProcess)
                                self.execute(executableProcess)
                                break

                    if len(self.waiting) == 0 and len(self.running) == 0:
                        # finished, enable the ok button and stop the timer
                        self.ui.ui.buttonBox.buttons()[0].setEnabled(True)
                        self.timer.stop()

        self.ui.ui.durationLabel.setText(QString(str(time.time() - self.startTime) + " seconds"))
        self.ui.ui.completedLabel.setText(QString(str(self.value)))
        self.ui.ui.remainingLabel.setText(QString(str(len(self.waiting) + len(self.running))))
