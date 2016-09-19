# Creating Arrays
grocery_list = %w(milk eggs bread)

other_list = []

list3 = Array.new

list_formerly_known_as_4 = ['thingy', 7]

#Adding to Arrays
grocery_list << 'yogurt'

grocery_list.push('potatoes')

grocery_list.unshift('broccoli')

grocery_list += ['ice cream', 'pie']

grocery_list << 7

grocery_list.insert(2, 'oatmeal')

grocery_list.unshift('celery')

# Getting items from Arrays

grocery_list[0]

grocery_list.at(1)

grocery_list[-1]

grocery_list.first

grocery_list.last

last = grocery_list.pop

first = grocery_list.shift

last_two = grocery_list.drop(2)

first_three = grocery_list.slice(0, 3)

# Array Properties

grocery_list.length

grocery_list.count

grocery_list.count('eggs')

grocery_list.include?('eggs')

grocery_list = %w(milk eggs bread ice\ cream pie potatoes)


puts grocery_list.inspect