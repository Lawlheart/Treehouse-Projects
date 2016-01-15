#### Peewee
_from peewee import *_

SqliteDatabase('databasename.db')
	returns the info for a new database saved as databasename.db in ./

class Student(Model):
	peewee models are python classes, passed in like so

class Meta: (inside Model class)
	database = db
		used to signify database and other settings


*MODEL FIELDS*
CharField(max_length=, unique=)
	signifies a character field on our model
	ex: username = CharField(max_length=255, unique=True)

IntegerField(default=)
	signifies a number field on our model
  ex:points = IntegerField(default=0)

TextField()
	signifies a text string of any length

DateTimeField(default=)
	signifies a datetime object, can set to timestamp like so:
	DateTimeField(default=datetime.datetime.now)


*RUNNING OUR DB*
if __name__ == '__main__': (if not imported i.e. if main process)
  db.connect()      			 (connect to the database)
  db.create_tables([Student], safe=True)   (create db, no err if exists)


*MODEL METHODS*
.create()  					# adds a new record to the table
.select() 					# lets us pick rows out of the table to use
.save() 						# updates an existing row in the database
.get() 							# will fetch a single record from the database
.delete_instance() 	# will delete a row from the table

.select().order_by(Model.propname.desc()).get()
	sorts the Model by propname in descending order. .asc() for ascending
	.get() returns the first record

.where(Model.propname.contains(search_string))
	filters items in the model by ones that contain the search string


#### SQLite 3 Console
_swlite3 databasename.db_ (on command line)

.tables
	prints out current tables in the db, signified by models

select * from student;
	prints all elements of the student table

.exit
	closes interface
