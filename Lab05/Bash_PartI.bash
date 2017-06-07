#! /bin/bash

#----------------------------------
# $Author: ee364c01 $
# $Date: 2017-02-14 17:08:18 -0500 (Tue, 14 Feb 2017) $
#----------------------------------

function part_a 
{               
    python3 practical1.py >> output.txt 2> output.txt            
}                               

function part_b
{              
    	
	#data=$(tail -n +1 people.csv)
	#echo $data
	data=$(sort -k6 -n people.csv)
}                              

function part_c
{
	Arr=($(ls src/*.c))
	for a in ${Arr[*]}
	do
		gcc $a 2> /dev/null 1> /dev/null
		if (( $? == 0 ))
		then 
			a=$(echo $a | cut -d'/' -f2)
			echo $a\:success
		else
			a=$(echo $a | cut -d'/' -f2)
			echo $a\:failure
		fi
	done    
}

function part_d
{
	Arr=(a.txt b.txt c.txt d.txt)
	((rand_num=$RANDOM%4))
	filename=${Arr[$rand_num]}
	cat $filename | head -n 6 |tail -n 2     
}

function part_e
{
	data=$(ping -c 3 ecegrid.ecn.purdue.edu)
	data1=$(echo $data | cut -d'=' -f11 | cut -d'/' -f2)
	echo $data1 ms
}

# To test your function, you can call it below like this:
#
part_a
part_b
part_c
part_e
