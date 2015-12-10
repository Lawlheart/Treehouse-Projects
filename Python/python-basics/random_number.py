# make a game that:
	#picks a random number 1-10
	#asks the user to guess a number
		#if the guess is too high or too low, tell them and let them guess again
		#if they guess the right number, congratulate them

	#EC: Limit the number of guesses
	#EC: Tell them how many guesses made

import random

def guessing_game(max_num, max_guesses):
	the_number = random.randint(1,max_num)
	print("AI as chosen a number from 1 to {}. You have {} guesses.".format(max_num, max_guesses))
	guesses = 0
	while True:

		guess_str = input("What is my number? ")

		try:
			guess = int(guess_str)
		except:
			print("That's not a whole number. Enter a valid number")
			continue

		if guess > max_num or guess < 0:
			print("guess out of range. Enter a valid number.")
			continue

		guesses = guesses + 1


		if guess == the_number:
			print("Congratulations, my number was indeed {}! You guessed the correct number after {} guesses.".format(the_number, guesses))
			break
		elif guesses == max_guesses:
			print("Max guesses reached! The number was {}. Play again!".format(the_number))
			break
		elif guess < the_number:
			print("Too low! You have {} guesses remaining".format(max_guesses - guesses))
			continue
		elif guess > the_number:
			print("Too high! You have {} guesses remaining".format(max_guesses - guesses))
			continue

guessing_game(10, 3)