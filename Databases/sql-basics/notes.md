- gets all items from table
`SELECT * FROM table;`

- get one column from table (named col_name)
`SELECT col_name FROM table;`

- get 2+ columns from table (named col1 and col2)
`SELECT col1, col2 FROM table;`

- Alias columns (col1 => Column)
`SELECT col1 as Column FROM table;`

- Alias with spaces (first_name => First Name)
`SELECT first_name as "First Name" FROM table;`
NOTE: may use ' ' or " " or {} depending on DB

- Can omit AS keyword (last_name => Last, etc)
`SELECT first_name First, last_name Last FROM table`

- Can use WHERE to filter results
`SELECT title, author FROM books WHERE published = 1997`

- Can chain conditions using AND or OR
`SELECT title FROM books WHERE author = "J.K. Rowling" AND first_published < 2000;`

- Can use IN to find multiple values on one Column
`SELECT * FROM table WHERE id IN (1, 4, 5)`

- Can use BETWEEN to find values in a range
`SELECT * FROM table where score BETWEEN 1 AND 4`
NOTE: range is *inclusive* on both ends

- Can use % as a wildcard and LIKE keyword to search
`SELECT title FROM books WHERE title LIKE "Harry Potter%";`

- Can use multiple %. Like searches are case-indep.
`SELECT title FROM books WHERE title LIKE "%universe%" AND genre LIKE "NoN fICTion";`

- Can use IS NULL to check if an entry is empty
`SELECT * FROM loans WHERE return_by > "2015-12-18" AND returned_on IS NULL;`

- Can use IS NOT NULL ensure the entry has a value
`SELECT * FROM loans WHERE return_by > "2015-12-18" AND returned_on IS NOT NULL;`

