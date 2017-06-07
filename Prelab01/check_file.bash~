#! /bin/bash

if (( $#!=1 ))
then
	echo "Usage: ./check_file.bash <filename>"
else
	Filename=$1
	printf "$Filename "
	if [[ ! -e $Filename ]]
	then 
		printf "not "
	fi
	printf "exists\n"
	printf "$Filename is "
	if [[ ! -d $Filename ]]
	then 
		printf "not "
	fi
	printf "a direcotry\n"
	printf "$Filename is "
	if [[ ! -f $Filename ]]
	then 
		printf "not "
	fi
	printf "an ordinary file\n"
	printf "$Filename is "
	if [[ ! -r $Filename ]]
	then 
		printf "not "
	fi
	printf "readable\n"
	printf "$Filename is "
	if [[ ! -w $Filename ]]
	then 
		printf "not "
	fi
	printf "writable\n"
	printf "$Filename is "
	if [[ ! -x $Filename ]]
	then 
		printf "not "
	fi
	printf "executable\n"

fi

