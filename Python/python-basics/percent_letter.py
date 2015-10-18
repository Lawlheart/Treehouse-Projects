user_string = input("What is your string? ")
user_num = input("What is your number? ")

try:
	our_num = int(user_num)
except:
	our_num = float(user_num)
	