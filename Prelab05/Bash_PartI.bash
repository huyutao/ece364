#! /bin/bash

#----------------------------------
# $Author$
# $Date$
#----------------------------------

function part_a 
{               
	myDir=~/myDir
	Arr=($(ls $myDir/*.pdf))
	cnt=0
	for a in ${Arr[*]}
	do
		((cnt++))
	done
	return $cnt           
}                               

function part_b
{              
	n=3
	cat data.txt | head -n $n |tail -n 1     
}                              

function part_c
{
	./userinput.o < input.txt
}

function part_d
{
	diff foo1.txt foo2.txt 2> /dev/null 1> /dev/null
	if [[ $? == 0 ]]
	then 
		echo Files are similar.
	else
		echo Files are different.
	fi
}

function part_e
{
    gcc windows8.c 2>> compile.out 1>> compile.out
}


# To test your function, you can call it below like this:
#
part_a
echo $?
part_b
part_c
part_d
part_e
