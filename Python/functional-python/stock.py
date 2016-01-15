from copy import copy
from functools import partial, reduce
import json
from operator import attrgetter, itemgetter

class Book:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title

    def __repr__(self):
        return str(self)


def get_books(filename, raw=False):
    try:
        data = json.load(open(filename))
    except FileNotFoundError:
        return []
    else:
        if raw:
            return data['books']
        return [Book(**book) for book in data['books']]
# RAW_BOOKS is just the json, whereas the Book class has been used on BOOKS
BOOKS = get_books('books.json')
RAW_BOOKS = get_books('books.json', raw=True)

# RAW_BOOKS is a list of book dictionaries
# pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))

# BOOKS is a list of instances of the Book class
# books_sort = sorted(BOOKS, key=attrgetter('number_of_pages'))


def sales_price(book):
    """Apply a 20% discount to the book's price """
    book = copy(book)
    book.price = round(book.price * 0.8, 2)
    return book

# sales_books = list(map(sales_price, BOOKS))


def is_long_book(book):
    """Does a book have more than 600 pages?"""
    return book.number_of_pages >= 600

# long_books = list(filter(is_long_book, BOOKS))


def has_roland(book):
    return any(["Roland" in subject for subject in book.subjects])


def titlecase(book):
    book = copy(book)
    book.title = book.title.title()
    return book

# print(list(map(titlecase, filter(has_roland, BOOKS))))


def is_good_deal(book):
    return book.price <= 5

# cheap_books = sorted(
#     filter(is_good_deal, map(sales_price, BOOKS)),
#     key=attrgetter('price')
# )
# print(cheap_books[0], cheap_books[0].price)


def product(x, y):
    return x * y

# print(reduce(product, [1, 2, 3, 4, 5]))

def add_book_prices(book1, book2):
    return book1 + book2

# total = reduce(add_book_prices, [b.price for b in BOOKS])

def long_total(a=None, b=None, books=None):
    if a is None and b is None and books is None:
        return None
    if a is None and b is None:
        a = books.pop(0)
        b = books.pop(0)
        return long_total(a, b, books)
    if a is not None and books and books is not None and b is None:
        b = books.pop(0)
        return long_total(a, b, books)
    if a is not None and b is not None and books is not None:
        return long_total(a + b, None, books)
    if a is not None and b is None and not books or books is None:
        return a

# print(long_total(None, None, [b.price for b in BOOKS]))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# print(factorial(5))

# RECURSIVE PROBLEM
courses = {'count': 2,
           'title': 'Django Basics',
           'prereqs': [{'count': 3,
                     'title': 'Object-Oriented Python',
                     'prereqs': [{'count': 1,
                               'title': 'Python Collections',
                               'prereqs': [{'count':0,
                                         'title': 'Python Basics',
                                         'prereqs': []}]},
                              {'count': 0,
                               'title': 'Python Basics',
                               'prereqs': []},
                              {'count': 0,
                               'title': 'Setting Up a Local Python Environment',
                               'prereqs': []}]},
                     {'count': 0,
                      'title': 'Flask Basics',
                      'prereqs': []}]}


def prereqs(data, pres=None):
    if pres is None:
        pres = set()
    else:
        pres.add(data['title'])
    if data['prereqs']:
        [prereqs(d, pres) for d in data['prereqs']]
    return pres

# print(prereqs(courses))

total = reduce(lambda x, y: x + y, [b.price for b in BOOKS])
# print(total)
long_books = filter(lambda book: book.number_of_pages >= 600, BOOKS)
# print(len(list(long_books)))
good_deals = filter(lambda book: book.price <= 5.99, BOOKS)
# print(len(list(good_deals)))

meals = [
    {'name': 'cheeseburger',
     'calories': 750},
    {'name': 'cobb salad',
     'calories': 250},
    {'name': 'large pizza',
     'calories': 1500},
    {'name': 'burrito',
     'calories': 1050},
    {'name': 'stir fry',
     'calories': 625}
]

high_cal = filter(lambda meal: meal['calories'] > 1000, meals)
# print(list(high_cal))


def mark_down(book, discount):
    book = copy(book)
    book.price = round(book.price * (1 - discount), 2)
    return book

standard = partial(mark_down, discount=0.2)
# print(standard(BOOKS[0]).price)
half = partial(mark_down, discount=0.5)
# print(half(BOOKS[0]).price)
half_price_books = map(half, filter(is_long_book, BOOKS))
# print(list(half_price_books))


def curried_f(x, y=None, z=None):
    def f(x, y, z):
        return x**3 + y**2 + z

    # returns the partial function with current variables saved

    if y is not None and z is not None: # if you have ALL x, y, z
        return f(x, y, z)                      #return as normal
    if y is not None:                   # if you have x and y, but NOT z
        return lambda z: f(x, y, z)         # z will be the next run's x!
    return lambda y, z=None: (          # if you have JUST x
        f(x, y, z) if (                     # setup for third run
        y is not None and z is not None)
        else (lambda z: f(x, y, z)))        # z will be the next run's x

print(curried_f(2, 3, 4))
g = curried_f(2)(3)(4)
print(g)

