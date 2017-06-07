#! /bin/bash

if [[ $# != 1 ]]
then 
	echo "Usage: process_temps.bash <input file>"
	exit 1
else
	if [[ ! -r $1 ]]
	then 
		echo "Error: $1 is not a readable file."
		exit 2
	else
		exec 3< $1
		read line <&3
		while read line <&3
		do
			arr=($line)
			((average=(${arr[1]}+${arr[2]}+${arr[3]}+${arr[4]})/4))
			echo "Average temperature for time ${arr[0]} was $average C."
		done
		exit 0
	fi
fi
