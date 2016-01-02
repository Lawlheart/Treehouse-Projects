List.index('thing')
	returns the index value of 'thing', works on strings and Lists, i.e. iterables. If thing is not present, emits an Error
print('thing', file=os.stdout)
	can use other things for file parameter
	steps to use file system

		set directory: 	dir_fd = os.open('./', os.O_RDONLY)
		make opener: 	 	def opener(path, flags):
					     					return os.open(path, flags, dir_fd=dir_fd)  
		print to dir:		print('thing', file = open('file.txt', 'w', opener=opener))
		close dir_fd: 	os.close(dir_fd)
	
	OR:
	
		set directory: 	dir_fd = os.open('./', os.O_RDONLY)
		print to dir:  	print('thing', file=open('file.txt', 'w', dir_fd))
		close dir:			os.close(dir_fd)