#### Sort
sorted()
	works like .sort(), but doesn't change original

#### itemgetter
_from operator import itemgetter_
	returns items in a list of collections of the specified key
	sorted(RAW_BOOKS, key=itemgetter('prop'))
		itemgetter is to sort by a dictionary key value
		unlike JS, dic.prop is NOT a valid way to get dictionary values
		use dic['prop']
#### attrgetter
_from operator import attrgetter_
	sorted(BOOKS, key=attrgetter('prop'))
		attrgetter is to sort by an object property key

#### Map
map(function, iterable)
	iterates over the iterator and passes each into the function
	ex: salesbooks = list(map(sales_price, BOOKS))

#### list comprehension
create list by using for loop, functionally similar to map()
	ex: [sales_price(book) for book in BOOKS]
		runs sales_price(book) for each book, adds returns to list
	can use to filter, too, like so:
	ex: [book for book in BOOKS if is_long_book(book)]

####  Filter
filter(filter_fun, iterable)
	longbooks = list(filter(is_long_book, BOOKS))

#### Chaining
any(iterable)
	returns true if any item in the iterable is true
	
#### Reduce
reduce(func, iterable)
	function needs to take in 2 args and return 1. 

#### Lambdas
inline functions for python. No assignments, and it returns the last line
	total = reduce(lambda x, y: x + y, [b.price for b in BOOKS])
		print(total) prints total price of all books
	long_books = filter(lambda book: book.number_of_pages >= 600, BOOKS)
		print(len(list(long_books))) prints number of long books
	good_deals = filter(lambda book: book.price <= 5.99, BOOKS)
		print(len(list(good_deals))) prints number of good deals

#### Currying
kind of makes a function return a partial result with partial variables
def curried_f(x, y=None, z=None):
    def f(x, y, z):
        return x**3 + y**2 + z
    if y is not None and z is not None:
        return f(x, y, z)
    if y is not None:
        return lambda z: f(x, y, z)
    return lambda y, z=None: (
        f(x, y, z) if (y is not None and z is not None)
        else (lambda z: f(x, y, z)))

stuff past our f function just return partial versions of our function depending on what variable we give. kind of like using closures in JS