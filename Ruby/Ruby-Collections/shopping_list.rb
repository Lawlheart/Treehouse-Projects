def create_list
  print 'What is the list name? '
  name = gets.chomp
  {name: name, items: []}
end

def add_list_item
  print 'What is the item called? '
  item_name = gets.chomp

  print 'How many? '
  quantity = gets.chomp.to_i

  {name: item_name, quantity: quantity}
end

def print_separator(character = '-')
  puts character * 80
end

def print_list(list)
  puts "\nList: #{list[:name]}"
  print_separator
  list[:items].each do |item|
    puts "Item: #{item[:name]}\t\t\tQuantity:#{item[:quantity]}"
  end
  print_separator
end

list = create_list
list[:items].push(add_list_item)
list[:items].push(add_list_item)
list[:items].push(add_list_item)
print_list(list)