def get_name
  print 'Enter your name: '
  gets.chomp
end

def greet(name)
  puts "Hi #{name}!"
  if name == 'Kenneth'
    puts 'Hey, that\'s my name, too!'
  end
end

def get_number
  print 'What number would you like to test? '
  gets.chomp.to_i
end

def divisible_by_three(number)
  number % 3 == 0
end

name = get_name
greet(name)
number = get_number

if divisible_by_three(number)
  puts 'Your number is divisible by three!'
else
  puts 'Your number is not divisible by three.'
end