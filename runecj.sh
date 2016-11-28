#!/bin/bash
# Original script provided by Dr. Michael Lones
# Command line arguments: number-of-repeats parameters-file
# Calculates the time in milliseconds for line 9 to run
# Probably reasonably inaccurate in calculating the "true" run time
for i in `seq 1 $1`; do
	echo "Run "$i
	ts=$(date +%s%N)
	java -cp . ec.Evolve -file $2 2> "output"$i".txt"
	tt=$((($(date +%s%N) - $ts)/1000000))
	echo "Time taken: $tt milliseconds"
	mv out.stat "out"$i".stat"
done
