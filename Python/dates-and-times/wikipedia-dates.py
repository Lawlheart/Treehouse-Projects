# Make a script that accepts a month and day date
# return a link to wikipedia of that date

import datetime


def wiki_dates():
    while True:
        print("What date would you like to search? Use MM/DD format")
        print("Enter 'quit' to quit")
        raw_date = input("> ")
        if raw_date.lower() == 'quit':
            break
        else:
            try:
                date = datetime.datetime.strptime(raw_date, "%m/%d")
                page = datetime.datetime.strftime(date, "%B_%d")
                print("\nhttps://en.wikipedia.org/wiki/{}\n".format(page))
            except ValueError:
                print("\nPlease enter a valid date.\n")

wiki_dates()
