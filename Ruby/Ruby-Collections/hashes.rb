# Hash Creation

item = Hash.new

item = {}

item = {"name" => "Bread"}

item["name"]

item = {"name" => "Bread", "quantity" => 1}

item = {"name" => "Bread", "quantity" => 1, 1 => "Grocery Store"}

item["brand"] = "Treehouse Bread Co."

item[:name] = "Bread"

item.delete(1)

item = {name: "Bread", quantity: 1}

# Hash Keys

hash = {item: 'Bread', quantity: 1, brand: 'Treehouse Bread Company'}

hash.keys # get array of keys

hash.has_key?(:brand)

hash.member?(:brand) # same as has_key?

hash.fetch(:brand) # same as hash[:brand]

hash == item

hash.store(:weight, '1 lb')

hash.values # gets array of values

hash.has_value?(1)

hash.values_at(:item, :quantity)

hash = {item: 'Bread', quantity: 1, brand: 'Treehouse Bread Company'}

puts "hash: #{hash.inspect}"

puts "hash.length: #{hash.length}"

puts "hash.invert: #{hash.invert}"

puts "hash.shift returns: #{hash.shift}"

puts "new hash is: #{hash.inspect}"

hash[:item] = 'Bread'

puts "merge with {calories: 100}: #{hash.merge({calories: 100})}"

puts "original hash is unchanged: #{hash}"

puts "merge with {item: 'Eggs'} (replaces item): #{hash.merge({item: 'Eggs'})}"
