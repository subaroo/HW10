#!/usr/bin/env python

# Imports
import random


# Body
def get_first_human_guess():
	'''Gets the first guess from the human'''
	human_guess = raw_input("Your turn: How many marbles will you remove (1-3)? ")
	return human_guess


def get_comp_guess():
	'''Get a guess from the computer'''
	comp_guess = random.randint(1,3)
	return comp_guess


def validate_human_guess(human_guess): 
	'''Tests the human's guess and makes sure the entry works'''
   	if (human_guess == 1) or (human_guess == 2) or (human_guess == 3):
   		print("human made good guess")
	    	check_jar(human_guess)
	    	if human_guess > marbles_left:
	    		print("Sorry there aren't that many marbles left. Try again!")
    		else:
    			print("You removed {0} marbles.".format(guess))
	elif (human_guess != 1) or (human_guess != 2) or (human_guess != 3):
		print("Sorry that's is not a valid entry. Try again!")

# after both go print out the # marbles removed and the  # marbles left
# if # marbles left = 0, declare the winner


def check_jar(human_guess):
	marbles_in_jar = 17
	if marbles_in_jar > human_guess:
		marbles_left = marbles_in_jar - human_guess
		marbles_in_jar = marbles_left
		return marbles_left
	else:
		return marbles_left










# ---------------------------------
def main():
	print("Let's play the game of Seventeen!")
	print("Number of marbles left in jar: 17 \n")
	human_guess = get_first_human_guess()
	get_comp_guess()
	validate_human_guess(human_guess)
    

if __name__ == '__main__':
    main()