shopping_list = []

def show_help():
	print('What should we pick up at the store? (Enter items separated by commas or individually). Enter \'HELP\' to repeat this message, \'SHOW\' to show your list, or \'DONE\' to stop. ')	

def add_to_list(item):
	shopping_list.append(item)
	print('Added! List has {} items'.format(len(shopping_list)))

def show_list():
	print('Here is your list:')
	print(', '.join(shopping_list))

show_help()
while True:
	new_item = input(">")
	if new_item == 'DONE':
		break
	elif new_item == 'HELP':
		show_help()
		continue
	elif new_item == 'SHOW':
		show_list()
		continue
	elif ',' in new_item:
		new_items = new_item.split(',')
		for item in new_items:
			add_to_list(item)
	else:
		add_to_list(new_item)

show_list()
