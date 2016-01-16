## Testing
****

`python3 -m doctest filename.py`
 - runs doctests from the shell

Python unit tests are written like so:
```python
"""this is the docstring...

    >>> cells = build_cells(2, 2)
    >>> m, d, p = get_locations(cells)
    >>> m != d and d != p
    True
    >>> d in cells
    True

"""
```
 - commands are denoted by >>>
 - lines without >>> are responses

## UNIT TEST
****
*import unittest*

`python3 -m unittest filename.py`
 - runs unit tests from shell. Can alternatively use:

```
if __name__ == '__main__':
	unittest.main()
```

Basic Assertion looks like so:

```
class MyTestCase(unittest.TestCase):
	def test_no1(self):
		assert 5 + 5 == 10
```
 - classes are made like so, inheriting from unittest.TestCase
 - tests MUST start with test_
 - use assert to say that a statement is true

```
class MyTestCase(unittest.TestCase):
	def setUp(self):
```
 - old method, still uses camelCase. used to set up variables
 - will run before EACH test


### TESTING OPTIONS
****
`assert 5 + 5 == 10`
 - simple asertion, will pass if statement evaluates to True

`assertEqual(a, b)`
 - will pass if a == b, ex: a=3, b=2 + 1

`assertNotEqual(a, b)`
 - will pass if a != b, ex: a=5, b='5'

`assertGreater(a, b)`
 - will pass if a > b, ex: a=4, b=3

`assertGreaterEqual(a, b)`
 - will pass if a >= b, ex: a=4, b=random.randint(4,10)

`assertLess(a, b)`
 - will pass if a < b, ex: a=3, b=4

`assertLessEqual(a, b)`
 - will pass if a <= b, ex: a=5, b=random.choice([3,4,5])

`assertTrue(a)`
 - will pass if a is True, ex: a = 3 > 2

`assertFalse(b)`
 - will pass if b is False, ex: b = 4 > 5

`assertIn(a, b)`
 - will pass if a in b ex: a=1, b=[1, 2, 3]

`assertNotIn(a, b)`
 - will pass if a not in b, ex: a=1, b=[3, 4, 5]

`assertIsInstance(a, b)`
 - will pass if a is an instance of b, ex: a=6, b=int

```
with assertRaises(ValueError):
	myfunction(a)
```
 - will pass if myfunction(a) raises a ValueError

`assertWarning()`
 - passes if code flags warning (need to look up syntax)

`assertLog()`
 - passes if code logs (need to look up syntax)


#### Coverage
****
*pip3 install coverage*

set up to auto-run:
```
if __name__ == '__main__':
    unittest.main()
```
first run
`coverage run test.py`
this will run tests

then run 
`coverage report`
to get test breakdown that looks like so:

```

	Name      Stmts   Miss  Cover
	-----------------------------
	dice.py      50     11    78%
	test.py      28      0   100%
	-----------------------------
	TOTAL        78     11    86%
```
then run 
`coverage report -m`
to get line-by-line breakdown that looks like:

```

	Name      Stmts   Miss  Cover   Missing
	---------------------------------------
	dice.py      50     11    78%   13-14, 26, 60, 63, 66, 69, 72-75
	test.py      28      0   100%
	---------------------------------------
	TOTAL        78     11    86%
```

Aim for about 90% or better coverage

can alternatively run 
`coverage html`
this makes a simply analytics site

then run 
`python3 -m http.server`
this opens the site at port 8000

command order:
`coverage run test.py`
`coverage html`
`python3 -m http.server`

You can mark lines for coverage to ignore
