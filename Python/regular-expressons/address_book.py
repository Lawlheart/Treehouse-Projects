import re

names_file = open('names.txt', encoding='utf-8')
data = names_file.read()
names_file.close()

# pr = re.match(r'Love', data)
# pr = re.search(r'Kenneth', data)
# pr = re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data)
# pr = re.search(r'\d{3} \d{3}-\d{4}', data)
# pr = re.search(r'\w+, \w+', data)
# pr = re.search(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data)
# pr = re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data)
# pr = re.findall(r'\w*, \w*', data)
# pr = re.findall(r'[-\w\d+.]+@[-\w\d.]+', data)
# pr = re.findall(r'\b[trehous]{9}\b', data, re.I)
# pr = re.findall(r'''
#     \b@[-\w\d.]* # find a word boundary, an @, and any number of characters
#     [^gov\t]+    # ignore 1 or more instances of the letters g, o, or v
#     \b           # match another word boundary
# ''', data, re.VERBOSE|re.I)
# pr = re.findall(r'''
#     \b[-\w]*,   # find a word boundary, 1+ hyphens or characters, and a comma
#     \s          # find one whitespace
#     [-\w ]+     # find 1+ hyphens and characters and explicit spaces
#     [^\t\n]     # ignore tabs and new line characters
# ''', data, re.X)

line = re.compile(r'''
   ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]*))\t  #last and first names
    (?P<email>[-\w\d.+]*@[-\w\d.]*)\t                   #emails
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t           #phone numbers
    (?P<job>[\w\s]*,\s[\w .]*)\t?                       #job and company
    (?P<twitter>@[\w\d]*)?$                             #twitter
''', re.X|re.M)


# print(re.search(line, data).groupdict())
# print(line.search(data).groupdict())
for match in line.finditer(data):
    print("{first} {last} <{email}>".format(**match.groupdict()))
