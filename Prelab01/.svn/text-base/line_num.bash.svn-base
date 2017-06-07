#! /bin/bash

if (( $#!=1 ))
then 
	echo "Error, one argument needed"
elif [[ -r $1 ]]
then
	exec 3< $1
	i=1
	while read line <&3
	do
		printf "$i:$line\n"
		((i=i+1))
	done
else
	printf "Cannot read $1\n"

fi
exit 0	

