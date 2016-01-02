# a word is chosen. 
# Player guesses a letter in the word
# if correct, reveals letter
# if wrong, loses a guess
# word is displayed after each guess

import random
import os
import sys

def get_word():
	words = []
	dir_fd = os.open('./', os.O_RDONLY)
	with open('words.txt', 'r', dir_fd) as wordfile:
		for word in wordfile:
			words.append(word.strip())
	return random.choice(words)

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def player_guess():
	valid_letters = list('abcdefghijklmnopqrstuvwxyz')
	guess = input("Guess a letter: ").strip()
	if guess.lower() not in valid_letters:
		return False
	else:
		return guess.lower()

def draw(word_list, correct, incorrect):
	clear()
	print("HANGMAN'S GALLEY")
	stickman(incorrect)
	output = []
	for letter in word_list:
		if letter in correct:
			output.append(letter)
		else:
			output.append("_")
	print("\n  {}\n".format("".join(output)))
	print("Correct: {}\nIncorrect: {}".format(''.join(correct), ''.join(incorrect)))

def stickman(incorrect):
	body_index = [42, 40, 33, 32, 31, 23]
	hangman = '  +--+  \n  |  |  \n  |  0  \n  | /|\ \n  | / \ \n  ======'
	hangman_list = list(hangman)
	if len(incorrect) <= 6:
		for part in range(0, len(incorrect)):
			hangman_list[body_index[part]] = " "
		print("".join(hangman_list))

def check_win(word_list, correct):
	for letter in word_list:
		if letter not in correct:
			return False
	return True

def game():
	print("Welcome to my hangman game! Press enter to start or enter 'q' to exit")
	start = input("> ")
	if start.lower() == 'q':
		sys.exit()
	word = get_word()
	word_list = list(word)
	correct = []
	incorrect = []
	draw(word_list, correct, incorrect)
	while True:
		guess = player_guess()
		if not guess:
			print("letters only please")
			continue
		elif guess in correct or guess in incorrect:
			print("You've already guessed that letter.")
			continue
		if guess in word_list:
			correct.append(guess)
			draw(word_list, correct, incorrect)
			print("\nCORRECT. {} is in the word!".format(guess))
			if check_win(word_list, correct):
				print("Congratulations! The word was indeed {}".format(word))
				break
		else:
			incorrect.append(guess)
			draw(word_list, correct, incorrect)
			print("\nINCORRECT. {} is not in the word!".format(guess))
			if len(incorrect) == 6:
				print("GAME OVER. The word was {}".format(word))
				break
	if input("Play again? y/n: ").lower() == 'y':
		game()	
	else:
		sys.exit()

game()