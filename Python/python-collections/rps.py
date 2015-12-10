import random
moves = ['rock', 'paper', 'scissors']

def game():
	#get player move, accounting for invalid entries
	while True: 
		player_move = input('rock, paper, or scissors: ')
		if player_move == 'rock' or player_move == 'paper' or player_move == 'scissors':
			print('Player chooses {}'.format(player_move))
			break
		else:
			print('invalid input')
			continue
	computer_move = moves[random.randint(0,2)]
	print('Computer chooses {}'.format(computer_move))
	win = compare(player_move, computer_move)
	if win:
		print("win!")
	else:
		print("lose!")
	

def compare(player_move, computer_move):
	if player_move == computer_move:
		print('Tie game')
		game()
	else:
		if player_move == 'rock':
			if computer_move =='paper':
				player_win = False
			elif computer_move == 'scissors':
				player_win = True
		elif player_move == 'paper':
			if computer_move == 'scissors':
				player_win = False
			elif computer_move == 'rock':
				player_win = True
		elif player_move == 'scissors':
			if computer_move == 'rock':
				player_win == False
			elif computer_move == 'paper':
				player_win == True
		return player_win


game()