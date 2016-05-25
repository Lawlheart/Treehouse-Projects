## Create

- Use INSERT to add data to tables
`INSERT INTO table VALUES (val1, val2, etc)`

- Use Auto Increment to add data to tables
`INSERT INTO table VALUES (NULL, val2, etc)`

- Can use names like so, can change order that way
`INSERT INTO loans (id, book_id, patron_id, loaned_on, return_by, returned_on) VALUES (NULL, 2, 4, "2015-12-14", "2015-12-21", NULL);`

- Can omit null values like so:
`INSERT INTO loans (book_id, patron_id, loaned_on, return_by) VALUES (2, 4, "2015-12-14", "2015-12-21");`

- Can enter multiple values at once like so:
```
INSERT INTO users 
        (id, username, password)
VALUES  (1, "Kreiger", "guest"),
        (2, "Archer", "glengoolie"),
        (3, "Cheryl", "matches")
```

## Update

- Can update using UPDATE
`UPDATE users SET password = "guest"`

- Can update multiple values like so:
`UPDATE users SET password = "guest", zip_code = 55555`

- Can use WHERE to filter changed rows
`UPDATE users SET password = "guest" WHERE username = "Kreiger"`

## Delete

- Can delete using DELETE. This deletes all rows.
`DELETE FROM users`


- Can filter delete with WHERE like other ops.
```
DELETE FROM patrons WHERE id = 4;
DELETE FROM loans WHERE patron_id = 4;
```

## Transactions

- Start with BEGIN or BEGIN TRANSACTION;
- End with COMMIT;
- Can revert with ROLLBACK;
- Changes aren't saved until COMMIT;