print 'What is your favorite number? '
number = gets.chomp.to_i

if number == 3 || number == 5
  puts 'That\'s my favorite number!'
elsif number > 10 && number.even?
  puts 'That\'s a pretty high, even number!'
elsif number.odd? && number % 3 == 0
  puts 'That number is divisible by 3 and is odd'
end