### Regular Expressions

re.match(rex, str, flag)
	matches starting at the beginning

re.search(rex, str, flag)
	matches anywhere

re.findall(rex, str, flag)
	finds any number of matches

MATCH.groupdict()
	use on search results to transform to dict using groups

MATCH.finditer(str)
	used to iterate over matches

MATCH.group(groupname or groupnum)
	returns the relevant group data

REGEX
	\w -> 	  any unicode word char: a-z, A-Z, 0-9, _
	\W -> !\w any not unicode word char
	\s ->     any whitespace
	\S -> !\s any non-whitespace
	\d ->     any number: 0-9
	\D -> !\d any non-number
	\b -> 		any word bounaries
	\B -> !\b any non-word boundaries

COUNTS
	{3} 	3 times
	{,3} 	at most 3 times
	{3,} 	at least 3 times
	{3,5} 3 to 5 times
	{?} 	0 or 1 times
	{*} 	at least 0 times
	{+} 	at least 1 time

SETS
	[aple] matches 'apple'
	[a-z]  matches all lowercase
	[^2]   matches NOT 2

FLAGS (3rd arg on re methods)
	re.IGNORECASE or re.I 	Ignores case on searches
	re.VERBOSE or re.X			handles multi-line regex
	re.MULTILINE or re.M		Treats each line as it's own string
	re.X|re.I 							add multiple flags separated by |

GROUPS
	\b([-\w]*),
		use () to signify a group.
	\b(?P<firstname>[-\w]*),
		use ?P<> to label a group name.