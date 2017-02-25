name = "Jason"

if defined?(name)
  name
else
  name = "Andrew"
end

puts name


new_name ||= "Andrew"

puts new_name


other_name = (other_name || "Nick")

puts other_name