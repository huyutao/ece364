#! /bin/bash

#---------------------------------------
# $Author: ee364c01 $
# $Date: 2017-01-24 17:28:43 -0500 (Tue, 24 Jan 2017) $
#---------------------------------------

# Do not modify above this line.  

while getopts f:o:-: foo 2> /dev/null
do

    case $foo in

	f) infile=$OPTARG
	    ;; #This means break
	o) outfile=$OPTARG
	    ;;
	-) if [[ $(echo $OPTARG | cut -d'=' -f1) == 'column_number' ]]
		then
			column_num=$(echo $OPTARG | cut -d'=' -f2)
		else
			echo "Invalid option." 
			exit 2
		fi
	   ;;
	# The variable $foo gets set to '?' when an invalid option is supplied.
	\?) echo "Invalid option." 
		exit 2
	    ;;

    esac
done


if [[ ! -r $infile ]]
then 
	echo "Error: Input file $infile is not readable."
	exit 3
else 
	col_in_file=$(head -n1 $infile | wc -w )
	if (( $col_in_file < $column_num ))
	then 
		echo "Error: Invalid column number."
		exit 4
	else
		echo "Sorting rows by column #$column_num."
		exec 3> $outfile
		sort -k$column_num -n $infile >&3
	fi
fi
exit 0
