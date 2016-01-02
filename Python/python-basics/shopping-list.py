## Shopping List
# make a list to hold onto our items
# print out instructions on how to use the app
# ask for new items to our list
# add new items to our list
# be able to quit the app
# print out the list

# steps to use file system
	# set directory: 	dir_fd = os.open('./', os.O_RDONLY)
	# make opener: 	 	def opener(path, flags):
	#				     	return os.open(path, flags, dir_fd=dir_fd)  
	# print to dir:		print('thing', file = open('file.txt', 'w', opener=opener))
	# close dir_fd: 	os.close(dir_fd)

	# OR:
		# set directory: 	dir_fd = os.open('./', os.O_RDONLY)
		# print to dir:  	print('thing', file=open('file.txt', 'w', dir_fd))
		# close dir:			os.close(dir_fd)

import os
shopping_list = []

def add_item(item):
	if ',' in item:
		for single in item.split(','):
			shopping_list.append(single.strip())
	else: 
		shopping_list.append(item.strip())
	print("Added {}. List now has {} items".format(item, len(shopping_list)))

def show_help():
	print("Welcome to my shopping list! Please enter your items now. ")
	print("Items may be separated by a comma")
	print("Enter DONE to finish")
	print("Enter SHOW to show your list.")
	print("Enter HELP to repeat this message.")
	print("Enter SAVE to save your list.")

def print_list():
	print("Here is your list:")
	for item in shopping_list:
		print(item)

def save_list():
	dir_fd = os.open('./', os.O_RDONLY)
	print('\n'.join(shopping_list), file = open('list.txt', 'w', dir_fd))
	os.close(dir_fd)
	print("{} items saved.".format(len(shopping_list)))

def main():
	show_help()
	while True:
		new_item = input("> ")
		if new_item == 'DONE':
			break
		elif new_item == 'HELP':
			show_help()
			continue
		elif new_item == 'SHOW':
			print_list()
			continue
		elif new_item == 'SAVE':
			save_list()
			continue
		add_item(new_item)
	print_list()
main()