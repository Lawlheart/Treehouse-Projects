try/except
	will do try unless it hits an error, then will do except instead

print('string')
	works like console.log

variable = input('question')
	asks a question in the console and puts the answer into variable

if 'thing' in variable
	checks to see if variable contains 'thing', similar to JS.indexOf() < 0

if var1 == var2
	== checks to see if the variables are equal

len('string') or len([1, 2, 3])
	gets length of strings or arrays

'string {}'.format(variable)
	works like JS variable concatenation to add variables to strings

list('string')
	works like JS.split(''), one item in the list per letter
	DOES NOT change 'string'

string_var.split()
	works like JS.split(' ') separating at the spaces to make a List. DOES NOT change the string_var
	By default, it breaks the string on spaces, tabs, or newlines.

'separator'.join(List_var)
	reverses split and joins a List into a string separated by the 'separator'
	ONLY works on strings, else will throw error
	DOES NOT change List_var

List_var.append()
	like JS.push(), adds the item to the end of the List. DOES change the List_var, appends a List as a List, not individual items

for item in List
	Python's "for" loop for Lists, with 'item' as an arbitrary name for List[i]

while True:
	loops until it sees a break. Infinite loops like this are probably more common in python because they have console user input, so they don't just crash.

break
	stops a loop

continue
	skips to the next loop


elif other_thing:
	elif is used to extend if gates

def function_name(argument):
	syntax for python functions