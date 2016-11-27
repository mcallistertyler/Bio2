#!/bin/bash

# Command line arguments: number-of-repeats parameters-file

for i in `seq 1 $1`; do
	echo "Run "$i
	ts=$(date +%s%N)
	java -cp . ec.Evolve -file $2 2> "output"$i".txt"
	tt=$((($(date +%s%N) - $ts)/1000000))
	echo "Time taken: $tt milliseconds"
	mv out.stat "out"$i".stat"
done