#! /bin/bash

#---------------------------------------
# $Author: ee364c01 $
# $Date: 2017-02-19 21:55:17 -0500 (Sun, 19 Feb 2017) $
#---------------------------------------

# Do not modify above this line.

wordlist=("banana" "parsimonious" "sesquipedalian")
((rand_num=$RANDOM%3))
word=${wordlist[rand_num]}
word_len=$(echo $word | wc -c)
((word_len-=1))

for ((i=0;i<$word_len;i++))
do
    guess_word[$i]='.'
    result_word[$i]=${word:$i:1}
done


echo "Your word is $word_len letters long"
echo "Word is: ${guess_word[*]}"
read -p "Make a guess: " guess_letter
echo ' '

good_go=0
for ((i=0;i<$word_len;i++))
do
	if [[ ${result_word[$i]} == $guess_letter ]]
	then 
		guess_word[$i]=$guess_letter
		good_go=1
	fi
done

finish=0
while [[ $finish == 0 ]]
do
	if [[ $good_go == 1 ]]
	then
		echo "Good going! Word is: ${guess_word[*]}"
	else
		echo "Sorry,try again. Word is: ${guess_word[*]}"
	fi

	read -p "Make a guess: " guess_letter
	echo ' '
	good_go=0
	for ((i=0;i<$word_len;i++))
	do
		if [[ ${result_word[$i]} == $guess_letter && ${guess_word[$i]} != $guess_letter ]]
		then 
			guess_word[$i]=$guess_letter
			good_go=1
		fi
	done

	if [[ ${guess_word[*]} == ${result_word[*]} ]]
	then
		echo "Good going!"
		echo "Congratulation! You guessed the word: $word"
		finish=1
	fi
	
done
