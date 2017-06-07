#! /bin/bash

if [[ $# != 2 ]]
then
	echo "Usage: run.bash <filename of simulator source code> <Output filename>"
else
	gcc $1 -o quick_sim
	if (( $? == 0 ))
	then 
		outfile=$2
		while [[ -e $outfile ]]
		do
			read -p "$2 exists.  Would you like to delete it? " ifdelete
			if [[ $ifdelete == 'y' || $ifdelete == 'yes' ]]
			then 
				rm $outfile
			else
				read -p "Enter a new filename: " outfile
			fi
		done
		exec 4>$outfile
		cache=(1 2 4 8 16 32)
		width=(1 2 4 8 16)
		fastest=999999
		fastest_result=0
		for c in ${cache[*]}
		do
			for w in ${width[*]}
			do
				result_a=$(./quick_sim $c $w a)
				result_b=$(./quick_sim $c $w i)
				echo $result_a | cut -d':' -f2,4,6,8,10 >&4
				echo $result_b | cut -d':' -f2,4,6,8,10 >&4
				speed_a=$(echo $result_a | cut -d':' -f10)
				speed_b=$(echo $result_b | cut -d':' -f10)

				if (( $speed_a < fastest ))
				then
					fastest=$speed_a
					fastest_result=$result_a 
				fi
				if (( $speed_b < fastest ))
				then
					fastest=$speed_b
					fastest_result=$result_b 
				fi
			done
		done
		fast_processor=$(echo $result_b | cut -d':' -f2)
		fast_cache=$(echo $result_b | cut -d':' -f4)
		fast_with=$(echo $result_b | cut -d':' -f6)
		fast_cpi=$(echo $result_b | cut -d':' -f8)
		echo "Fastest run time achieved by $fast_processor with cache size $fast_cache and issue width $fast_with was $fastest "
	else
		echo "error: quick_sim could not be compiled!"
	fi
fi
