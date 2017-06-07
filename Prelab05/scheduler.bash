#! /bin/bash

#----------------------------------
# $Author$
# $Date$
#----------------------------------

# Do not modify above this line.

if [[ $# != 1 ]]
then 
	echo "Usage: scheduler.bash <input file>"
	exit 1
else
	if [[ ! -r $1 ]]
	then 
		echo "Error: $1 is not a readable file."
		exit 2
	else
		name_space=8
		time_space=6
		time=(07:00 08:00 09:00 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00)
		exec 2> schedule.out
		exec 3< $1
		for ((i=0; i<11; i++))
		do
			total[i]=0
		done
		printf ' %.0s' {1..8} >&2
		for t in ${time[*]}
		do 
			echo -n $t '' >&2
		done
		echo "">&2
		while read line <&3
		do
			name=$(echo $line | cut -d' ' -f1)
			time=$(echo $line | cut -d' ' -f2)
			echo -n $name >&2
			((len=8-${#name}))
			for ((i=$len;i>0;i--))
			do
				echo -n ' ' >&2
			done
			for ((i=0; i<11; i++))
			do
				result[$i]='-'
			done
			Arr=($(echo ${time//,/ }))
			for variable in ${Arr[*]}
			do
				t=$(echo -n $variable | cut -d':' -f1)
				((t=t-7))
				result[$t]='Y'
				((total[$t]++))
			done
			for ((i=0; i<11; i++))
			do
				echo -n ${result[$i]} "    " >&2
			done
			echo '' >&2
		done
		echo "        " >&2
		echo -n "Total   " >&2
		max_av=0
		max_t=0
		for ((i=0; i<11; i++))
		do
			echo -n ${total[$i]} "    " >&2
			if (( ${total[$i]} > $max_av ))
			then 
				max_av=${total[$i]}
				max_t=$i
			fi
		done
		echo "" >&2
		((max_t+=7))
		echo The maximum number of people are available at $max_t\:00.
		exit 0
	fi
fi
