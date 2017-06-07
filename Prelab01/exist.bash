#! /bin/bash

Num_Of_Param=$#
for((i = 0; i < $Num_Of_Param;i++))
do
	filename=$1
	if [ -r $filename ]
	then
		printf "File $filename is readable\n"
	else
		touch $filename
	fi
	shift
done
exit 0	

