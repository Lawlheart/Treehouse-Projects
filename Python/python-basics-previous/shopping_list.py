shopping_list = []
	# list() works as well
print("What should we pick up at the store? ")
print("Items may be separated by commas or entered individually.")
print("Enter 'DONE' to stop adding items. ")

while True:
	new_item = input("> ")

	if new_item == 'DONE':
		break
	elif ',' in new_item:
		new_items = new_item.split(',')
		for item in new_items:
			shopping_list.append(item)
	else:
		shopping_list.append(new_item)


	print("Added! List has {} items.".format(len(shopping_list)))
	continue

print("Here is your list:")

list = []

for item in shopping_list:
	list.append(item)

print(', '.join(list))