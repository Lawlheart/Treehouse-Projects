PEP 8
	flake8 to lint python

PEP 20
	The Zen of Python, by Tim Peters
	Beautiful is better than ugly.
	Explicit is better than implicit.
	Simple is better than complex.
	Complex is better than complicated.
	Flat is better than nested.
	Sparse is better than dense.
	Readability counts.
	Special cases aren't special enough to break the rules.
	Although practicality beats purity.
	Errors should never pass silently.
	Unless explicitly silenced.
	In the face of ambiguity, refuse the temptation to guess.
	There should be one-- and preferably only one --obvious way to do it.
	Although that way may not be obvious at first unless you're Dutch.
	Now is better than never.
	Although never is often better than *right* now.
	If the implementation is hard to explain, it's a bad idea.
	If the implementation is easy to explain, it may be a good idea.
	Namespaces are one honking great idea -- let's do more of those!

Logging
	import logging
	logging.info("doesn't print to the player")
	logging.warn("Might print, depending on settings")
	logging.baseConfig(filename='filename.log', level=logging.DEBUG)
	*Levels*
		Critical		
		Error				
		Warning			.warn()
		Info				.info()
		Debug				.debug()
		NotSet

Debugger
	import pdb
	pdb.set_trace() at debug location
	n					goes to next line while debugging
	q  				quits pdb
	c 				finishes code
	myvar			prints myvar
	most common use:
		import pdb; pdb.set_trace()
		ONLY time python uses ;