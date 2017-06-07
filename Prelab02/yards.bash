#! /bin/bash

if [[ $# != 1 ]]
then 
	echo "Usage: yards.bash <filename>"
else
	Filename=$1
	if [[ ! -r $Filename ]]
	then 
		echo "Error: $Filename fakefile is not readable"
	else 
		largest_avg=0
		exec 3< $Filename
		while read line <&3
		do 
			arr=($line)
			yards_sum=0
			yards_var=0
			count=${#arr[*]}
			for ((i=1;i<count;i++))
			do
				((yards_sum+=${arr[i]}))
			done
			((average=$yards_sum/(($count-1)) ))
			for ((i=1;i<count;i++))
			do
				((yards_var+=(( ((${arr[i]} - average))*((${arr[i]} - average)) )) ))
			done
			((yards_var/=(($count-1)) ))
			echo "${arr[0]} schools averaged $average yards receiving with a variance of $yards_var"
			if((average>largest_avg))
			then
				largest_avg=$average
			fi
		done
		echo "The largest average yardage was $largest_avg"
	fi
fi
