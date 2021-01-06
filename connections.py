import sqlite3

def create_table_userdata():
	db = sqlite3.connect('data.db')
	curse = db.cursor()

	curse.execute("CREATE TABLE userdata (\
				   Username VARCHAR(256) UNIQUE,\
				   Password VARCHAR(256), \
				   Email VARCHAR(256))\
				   ")

	db.commit()
	db.close() 

def result():
	db = sqlite3.connect('data.db')
	curse = db.cursor()

	curse.execute("SELECT *, oid FROM userdata")
	results = curse.fetchall()

	db.commit()
	db.close()

	return result