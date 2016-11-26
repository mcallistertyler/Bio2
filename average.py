#Tyler McAllister
#H00153533
#Biologically Inspired Computation Coursework 2
#Works on Linux systems only!
#Runs the script that runs ECJ and puts all relevant outputs into a file
#Then very inefficiently takes the standardisation averag, average hits and standard deviation
#Only works with the runecj.sh file I have edited.

import os
import sys
import time
import numpy as np
from sys import stdin, stdout, argv

#Spins because spinning is fun
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor
print("Enter the number of iterations.\n")
userinput = stdin.readline()
#To use a different .params file change the file path here
print("./runecj.sh " + userinput.strip("\r\n") + " cw2/sextic_regression.params")
os.system("./runecj.sh " + userinput.strip("\r\n") + " cw2/sextic_regression.params")
os.system("echo \"Emptied...\" > work.txt")
spinner = spinning_cursor()
for _ in range(20):
    sys.stdout.write(spinner.next())
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')
for x in range(1, int(userinput)+1):
	os.system("echo " + "\"" + str(x) + "\"" + " >> work.txt" )
	os.system("ls -1 output" + str(x) +".txt | xargs tail -q -n 1 >> work.txt")
print "Outputs saved to file.\n"
stand = []
hits = []
with open('work.txt', 'r') as f:
	for line in f:
		if len(line) < 50:
			continue
		fields = line.split('=')
		stand.append(float(fields[1].split()[0]))
		hits.append(float(fields[3].split()[0]))
#Saves relevant results to a file 'averageresults.txt' but prints
#other values that may be useful into the terminal.
print stand
print "Average Fitness...", sum(stand) / len(stand)
averagestand = sum(stand) / len(stand)
print "\n"
print hits
print "Average Hits...", sum(hits) / len(hits)
averagehits = sum(hits) / len(hits)
print "\n"
print "Standard Deviation...",  np.std(stand)
print "Writing averages to file..."

f = open('averageresults.txt', 'w')
f.write("Average Standardisation: " + str(averagestand))
f.write("\n")
f.write("Average Hits : " + str(averagehits))
f.close()
