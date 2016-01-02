

import random

def computer_guess(low, high):
	return random.randint(low, high)

def game(low, high, max_guesses):
	num_range = [low, high]
	guesses = []
	print("Welcome to the Number Guessing Game - B sides! This time, the computer guesses YOUR number!")
	input("Think of a number between {} and {}. Press enter when ready.".format(low, high))
	while True:
		guess = computer_guess(num_range[0], num_range[1])
		print("Computer guesses {}. Is that your number?".format(guess))
		response = input("Enter YES if it is your number, HIGH if it's too high, or LOW if it's too low: ")
		guesses.append(guess)
		if response == 'YES':
			print("The computer got your number in {} guesses! ".format(len(guesses)))
			break
		elif response != 'YES' and len(guesses) == max_guesses:
			print("Computer has run out of guesses! Play again.")
			break
		elif num_range[0] == num_range[1]:
			print("No cheating! Try again.")
			break
		elif response == 'HIGH':
			num_range[1] = guess - 1
			print("Alright, the Computer is going to guess again.")
			continue
		elif response == 'LOW':
			num_range[0] = guess + 1
			print("Alright, the Computer is going to guess again.")
			continue
		else:
			print("Invalid input. Try again.")
			break


game(1, 10, 3)