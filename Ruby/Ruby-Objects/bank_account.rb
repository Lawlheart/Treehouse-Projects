class BankAccount
  attr_reader :name

  def initialize(attrs)
    @name = attrs[:name]
    @transactions = []
    add_transaction("Beginning Balance", 0)
  end

  def credit(description, amount)
    add_transaction(description, amount)
  end

  def debit(description, amount)
    add_transaction(description, -amount)
  end

  def add_transaction(description, amount)
    @transactions.push({:description => description, :amount => amount})
  end

  def balance
    balance = 0.0
    @transactions.each do |transaction|
      balance += transaction[:amount]
    end
    sprintf("%0.2f", balance)
  end

  def to_s
    "Name: #{name}, Balance: #{balance}"
  end

  def print_register
    puts "#{name}'s Bank Account"
    puts "="*40
    puts "Description".ljust(30) + "Amount".rjust(10)
    @transactions.each do |t|
      puts t[:description].ljust(30) + sprintf("%0.2f", t[:amount]).rjust(10)
    end
    puts "="*40
    puts "Balance:".ljust(30) + balance.to_s.rjust(10)
  end
end