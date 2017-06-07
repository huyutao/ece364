#! /bin/bash

exec 3< file_list
while read Filename <&3
do
	status=$(svn status $Filename | cut -c1)
	if [[ $status == '?' ]]
	then
		if [[ ! -x $Filename ]]
		then 
			read -p "do you want to make $Filename executable?" executable
			if [[ $executable == 'y' ]]
			then
				chmod +x $Filename
			fi
		fi
		svn add $Filename
	else
		if [[ ! -e $Filename ]]
		then 
			echo "Error: File $Filename appears to not exist here or in svn"
		else
			if [[ ! -x $Filename ]]
			then 
				svn propset svn:executable ON $Filename
			fi
		fi
	fi
done
svn commit
echo "Auto-committing code"




