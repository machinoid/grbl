#!/usr/bin/env python
"""\
Simple g-code streaming script for grbl

Provided as an illustration of the basic communication interface
for grbl. When grbl has finished parsing the g-code block, it will
return an 'ok' or 'error' response. When the planner buffer is full,
grbl will not send a response until the planner buffer clears space.

G02/03 arcs are special exceptions, where they inject short line 
segments directly into the planner. So there may not be a response 
from grbl for the duration of the arc.
"""

import sys
import subprocess
import time

# Open grbl
proc = subprocess.Popen("../grbl", shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)

# Open g-code file
f = open('grbl.gcode','r');

# Wake up grbl
proc.stdin.write("\r\n\r\n")
time.sleep(2)   # Wait for grbl to initialize 
# Flush startup text in input
while True:
    print 'Reading: '
    nextline = proc.stdout.readline()
    nextline = nextline.strip()
    print nextline
#    if nextline == "Grbl 0.8c ['$' for help]" and proc.poll() != None:
    if nextline == "Grbl 0.8c ['$' for help]":
        break

# Stream g-code to grbl
for line in f:
    l = line.strip() # Strip all EOL characters for consistency
    print 'Sending: ' + l
    proc.stdin.write(l + '\n') # Send g-code block to grbl
    proc.stdin.flush()
    print 'Reading: '
    grbl_out = proc.stdout.readline() # Wait for grbl response with carriage return
    print ' : ' + grbl_out.strip()
    time.sleep(0.1)

# Wait here until grbl is finished to close file.
raw_input("  Press <Enter> to exit and disable grbl.") 

# Close file
f.close()
