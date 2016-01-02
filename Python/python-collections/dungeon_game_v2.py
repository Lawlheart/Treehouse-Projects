## Dungeon Game made as part of TeamTreehouse Curriculum

import os
import sys
import random


# 3x3 grid, monster and door locations are HIDDEN in this version, monster stays still.

CELLS = [ (0, 0), (1, 0), (2, 0),
					(0, 1), (1, 1), (2, 1),
					(0, 2), (1, 2), (2, 2)	]

MAP = [	"  _______________________",
				" |       |       |       |",
				" |       |       |       |",
				" |_______|_______|_______|",
				" |       |       |       |",
				" |       |       |       |",
				" |_______|_______|_______|",
				" |       |       |       |",
				" |       |       |       |",
				" |_______|_______|_______|"]

MONSTER = ["\█Θ█/", 
					 " ███ ", 
					 "_/_\_"]
PLAYER = ["  O  ", 
					" /|\ ", 
					"_/_\_"]
DOOR = [" ___ ",
				"|  .|",
				"|___|"]
BREAD = ["     ",
				 "  X  ",
				 "_____"]

def generate_map(monster_loc, door_loc, player_loc, visited):
	
	clear()
	dungeon = MAP[:]
	for item in visited:
		dungeon = add_icon(dungeon, BREAD, item)
	if player_loc == monster_loc:
		dungeon = add_icon(dungeon, MONSTER, monster_loc)
	elif player_loc == door_loc:
		dungeon = add_icon(dungeon, DOOR, door_loc)
	else:
		dungeon = add_icon(dungeon, PLAYER, player_loc)
	for line in dungeon:
		print(line)

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def add_icon(dungeon, icon, location):
	x = location[0] + 1	# cols are (x*8-5, x*8)
	y = location[1] # rows are 3y+1, 3y+2, 3y+3
	lines = (3*y + 1, 3*y + 2, 3*y + 3)
	segment = (x*8-5, x*8)
	index = 0
	for line in lines:
		dungeon[line] = dungeon[line][:segment[0]] + icon[index] + dungeon[line][segment[1]:]
		index += 1
	return dungeon


def get_locations():
	# randomize monster, door, start
	monster_loc = random.choice(CELLS)
	door_loc = random.choice(CELLS)
	player_loc = random.choice(CELLS)
	# reroll all if any match
	if monster_loc == door_loc or door_loc == player_loc or player_loc == monster_loc:
		return get_locations()
	# else return monster, door, start
	else:
		return monster_loc, door_loc, player_loc

def get_moves(location):
	x, y = location
	# moves = up, down, left, right
	moves = [(x+1, y),(x-1, y),(x, y-1),(x, y+1)]
	move_names = ["RIGHT", "LEFT", "UP", "DOWN"]
	# remove illegal moves
	legal_moves = []
	index = 0
	for move in moves:
		if move in CELLS:
			legal_moves.append(move_names[index])
		index += 1	
	return legal_moves

def move_player(player_loc, move):
	x = player_loc[0]
	y = player_loc[1]
	if move.upper() == "RIGHT":
		return (x+1, y)
	elif move.upper() == "LEFT":
		return (x-1, y)
	elif move.upper() == "UP":
		return (x, y-1)
	elif move.upper() == "DOWN":
		return (x, y+1)

def game(): 
	visited = []
	locations = get_locations()
	monster_loc, door_loc, player_loc = locations
	generate_map(monster_loc, door_loc, player_loc, visited)
	print("Welcome to the dungeon!")
	while True:
		print("You're currently in room {}".format(player_loc)) # add player pos
		print("Available moves: {}".format(", ".join(get_moves(player_loc)))) # add available moves
		print("Enter QUIT to quit")

		move = input("> ").upper()
		if move == "QUIT":
			print("Goodbye!")
			sys.exit()
		#if it's a bad move, do nothing
		elif move not in get_moves(player_loc):
			print("invalid move")
			continue
		#if it's a good move, change the player's position
		else:
			visited.append(player_loc)
			player_loc = move_player(player_loc, move)
			generate_map(monster_loc, door_loc, player_loc, visited)
			if player_loc != door_loc and player_loc != monster_loc:
				continue
			#if the new position is the door, they win!
			elif player_loc == door_loc:
				print("CONGRATULATIONS! You found the door, you win!")
				break
			#if the new position is the monster, they lose!
			elif player_loc == monster_loc:
				print("You stumbled upon a room with a monster! GAME OVER")
				break

	# check if player wants to play again
	if input("Play again? y/n ").lower() == 'y':
		game()
	else:
		sys.exit()


game()