#! /bin/bash

#---------------------------------------
# $Author: ee364c01 $
# $Date: 2017-01-17 16:26:04 -0500 (Tue, 17 Jan 2017) $
#---------------------------------------

# Do not modify above this line.

if [[ $# != 2 ]]
then 
	echo "Usage: collect_stats.bash <file> <sport>"
	exit 1
else
	Filename=$1
	if [[ ! -e $Filename ]]
	then 
		echo "Error: $Filename does not exist"
		exit 2
	else 
		total_athletes=0
		total_medals=0
		max_medals=0
		max_athlete=0
		exec 3< $Filename
		while read line <&3
		do 
			if [[ $2 == $(echo $line | cut -d, -f2) ]]
			then 
				((total_athletes++))
				cur_medals=$(echo $line | cut -d, -f3)
				((total_medals+=cur_medals))
				if (( $cur_medals > $max_medals ))
				then
					((max_medals=cur_medals))
					max_athlete=$(echo $line | cut -d, -f1)
				fi
			fi
		done
		echo "Total athletes: $total_athletes"
		echo "Total medals won: $total_medals"
		echo "$max_athlete won the most medals: $max_medals"
	fi
	exit 0
fi
