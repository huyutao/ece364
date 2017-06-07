#! /bin/bash

#---------------------------------------
# $Author$
# $Date$
#---------------------------------------

# Do not modify above this line.

while getopts a:bc:-: foo
do

    case $foo in

	a) echo "You entered the argument '$OPTARG' for the option '-$foo'"
	    ;; #This means break

	b) echo "You entered the argument '$OPTARG' for the option '-$foo'"
	    ;;

	c) echo "You entered the argument '$OPTARG' for the option '-$foo'"
	    ;;

	-) echo "You entered '$OPTARG'."
	   ;;

	# The variable $foo gets set to '?' when an invalid option is supplied.
	\?) echo "Invalid option."
	    ;;

        # Default case
	*) echo "Default case."
	    ;;

    esac

done

exit 0