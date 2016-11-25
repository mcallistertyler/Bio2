#Tyler McAllister
#H00153533
#Biologically Inspired Computation Coursework 2
#Runs the script that runs ECJ and puts its outputs into a file
#Then very inefficiently takes the standardisation average and average hits

#Run in ecj folder and stuff
import os
from sys import stdin, stdout, argv
userinput = stdin.readline()
print("./runecj.sh " + userinput.strip("\r\n") + " cw2/santa_fe_ant.params")
os.system("./runecj.sh " + userinput.strip("\r\n") + " cw2/santa_fe_ant.params")
os.system("echo \"Emptied...\" > work.txt")
for x in range(1, int(userinput)+1):
	print "Output", x, " saved to file.\n"
	os.system("echo " + "\"" + str(x) + "\"" + " >> work.txt" )
	os.system("ls -1 output" + str(x) +".txt | xargs tail -q -n 1 >> work.txt")

stand = []
hits = []
with open('work.txt', 'r') as f:
	for line in f:
		if len(line) < 50:
			continue
		fields = line.split('=')
		stand.append(float(fields[1].split()[0]))
		hits.append(float(fields[3].split()[0]))

print stand
print "Average Standardisation...", sum(stand) / len(stand)
averagestand = sum(stand) / len(stand)
print "\n"
print hits
print "Average Hits...", sum(hits) / len(hits)
averagehits = sum(hits) / len(hits)
print "Writing averages to file..."

f = open('averageresults.txt', 'w')
f.write("Average Standardisation: " + str(averagestand))
f.write("\n")
f.write("Average Hits : " + str(averagehits))
f.close()
