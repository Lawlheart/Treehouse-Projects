# 2-d maze game
	# random locations for player, monster, door
	# player moves to try to find the door before the monster gets him
	# need a grid of rooms (coordinates)
	# 	place player, door, monster at random rooms

	# 	let player move

	# 	EC: Show Visual Map

import random
import os
import sys

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def get_squares(r):
	x, y = r
	lines = (y*3-2, y*3-1, y*3)
	segment = (x*8-5, x*8)
	return (lines, segment)

def randomize_start(num):
	coords = []
	for unit in range(num):
		while True:
			new_coord = (random.randint(1,6), random.randint(1,6))
			if new_coord not in coords:
				coords.append(new_coord)
				break
			else:
				continue
	return coords

def render_units(maze, units, coords):
	index = 0
	for unit in units:
		coord = coords[index]
		unit_lines, unit_seg = get_squares(coord)
		count = 0
		for line in unit_lines:
			maze[line] = maze[line][:unit_seg[0]] + unit[count] + maze[line][unit_seg[1]:]
			count += 1
		index += 1
	return maze

def update_maze(maze):
	clear()
	print("\n")
	for line in maze:
		print(line)
	print("\n")

def player_move(coord):
	valid_moves = ['up', 'down', 'left', 'right', 'w', 'a', 's', 'd']
	while True:
		d = input("Which direction will you move? (up, down, left, right)").lower().strip()
		if d not in valid_moves:
			print("invalid move")
			continue
		break
	return move(d, coord)

def monster_move(mon_coord, pl_coord):
	flip = random.randint(1,2)
	if mon_coord == pl_coord:
		return mon_coord
	elif mon_coord[0] == pl_coord[0] or mon_coord[1] != pl_coord[1] and flip == 1:
		if mon_coord[1] > pl_coord[1]:
			return move('up', mon_coord)
		else:
			return move('down', mon_coord)
	elif mon_coord[1] == pl_coord[1] or mon_coord[0] != pl_coord[0] and flip == 2:
		if mon_coord[0] > pl_coord[0]:
			return move('left', mon_coord)
		else:
			return move('right', mon_coord)

def move(d, coord):
	if d == 'up' or d == 'w' and coord[1] > 1:
		new_coord = (coord[0], coord[1] - 1)
	elif d == 'down' or d == 's' and coord[1] < 6:
		new_coord = (coord[0], coord[1] + 1)
	elif d == 'left' or d == 'a' and coord[0] > 1:
		new_coord = (coord[0] - 1, coord[1])
	elif d == 'right' or d == 'd' and coord[0] < 6:
		new_coord = (coord[0] + 1, coord[1])
	return new_coord

def game():
	maze=["  _______________________________________________",
				" |       |       |       |       |       |       |",
				" |       |       |       |       |       |       |",
				" |_______|_______|_______|_______|_______|_______|",
				" |       |       |       |       |       |       |",
				" |       |       |       |       |       |       |",
				" |_______|_______|_______|_______|_______|_______|",
				" |       |       |       |       |       |       |",
				" |       |       |       |       |       |       |",
				" |_______|_______|_______|_______|_______|_______|",
				" |       |       |       |       |       |       |",
				" |       |       |       |       |       |       |",
				" |_______|_______|_______|_______|_______|_______|",
				" |       |       |       |       |       |       |",
				" |       |       |       |       |       |       |",
				" |_______|_______|_______|_______|_______|_______|",
				" |       |       |       |       |       |       |",
				" |       |       |       |       |       |       |",
				" |_______|_______|_______|_______|_______|_______|"]
	monster = ["\█Θ█/", 
						 " ███ ", 
						 "_/_\_"]
	player = ["  O  ", 
						" /|\ ", 
						"_/_\_"]
	door = [" ___ ",
					"|  .|",
					"|___|"]
	units = (door, player, monster)
	coords = randomize_start(3)

	rendered_maze = render_units(maze[:], units, coords)
	door_coord, player_coord, monster_coord = coords

	update_maze(rendered_maze)

	while True:
		player_coord = player_move(player_coord)
		monster_coord = monster_move(monster_coord, player_coord)

		coords = door_coord, player_coord, monster_coord

		rendered_maze = render_units(maze[:], units, coords)
		update_maze(rendered_maze)

		if player_coord == monster_coord:
			print("GAME OVER!")
			break
		elif player_coord == door_coord:
			print("PLAYER WIN!")
			break

	if input("play again? y/n >").lower().strip() == 'y':
		game()
	else:
		sys.exit()

game()

# 6x6 grid, 19 lines (1 top + 3x each square) each square is | 7s |
# 6x 7 whitespace, 7x |, one spacer at start = 50
# line length 50 lines: [3:8], [12:17]
