# generate a random number between 1 and 10
# get a number guess from the player
# compare guess to secret number
# print hit/miss

import random

def game(max_num, max_guesses):
	computer_num = random.randint(1,max_num)
	correct_guess = False
	guesses = []
	print("Computer has chosen a number from 1 to {}. You have {} guesses. What is the number? ".format(max_num, max_guesses))
	while True:
		try:
			guess = int(input("> "))
		except ValueError:
			print("numbers only please.")
			continue
		else:
			guesses.append(guess)
			if guess != computer_num and len(guesses) == max_guesses:
				print("Sorry, my number was {}. Please try again!".format(computer_num))
				break

			elif guess > computer_num:
				print("Too high! You have {} tries remaining, guess again.".format(max_guesses - len(guesses)))
				continue
			elif guess < computer_num:
				print("Too low! You have {} tries remaining, guess again.".format(max_guesses - len(guesses)))
				continue
			elif guess == computer_num:
				print("Correct, the number was {}!. You guessed the correct number in {} tries.".format(computer_num, len(guesses)))
				break
	if input("Play again? Enter 'Y' for yes: ") == 'Y':
		print("Restarting game!\n\n")
		game(max_num, max_guesses)
game(10, 3)