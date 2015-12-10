range(num)
	makes an of numbers counting from 0-(num-1)
	(check help for range for other options?)
for i in range(100)
	works like for(var i=0;i<100;i++) in JS

[1,2,3] + [4,5,6]
	List addition works like JS.concat()

List.extend(List_2)
	also works like JS.concat, Changes List

List.insert(i, 'item')
	adds 'item' to the List at index i

List.index('thing')
	finds the index of 'thing', like JS.indexOf('thing')

del List[i]
	deletes the item at index i in List

List.remove('thing')
	removes the FIRST instance of 'thing' from the list

item_i = List.pop(i)
	removes the item at index i and returns it to item_i. using the method without i pulls the last item in the List