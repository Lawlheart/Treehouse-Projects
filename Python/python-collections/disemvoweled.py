#take a list of words
#remove all of the vowels in all of the words
#return the remaining vowel-free words

raw_words = input('Give me some words separated by commas to eradicate those pesky vowels from! ')
words = raw_words.split(',')

#words = ['fire', 'air', 'water','earth']
vowels = ['a','e','i','o','u']
new_words = []
for word in words:
	word_list = list(word.lower())
	for vowel in vowels:
		while True:
			try:
				word_list.remove(vowel)
			except:
				break
	new_words.append(''.join(word_list).capitalize())

print('{} becomes {}'.format(words, new_words))
