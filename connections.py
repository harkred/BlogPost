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

def create_table_blog():
	db = sqlite3.connect('data.db')
	curse = db.cursor()

	curse.execute("CREATE TABLE blog (\
				   bid INT,\
				   Blog_name VARCHAR(256), \
				   Blog_content Text)\
				   ")

	db.commit()
	db.close()    


   
def insert_blog(bid, blog_name, blog_content):
	db = sqlite3.connect('data.db')
	curse = db.cursor()

	curse.execute("INSERT INTO blog VALUES(\
                   :bid=bid, \
                   :Blog_name=Blog_name, \
                   :Blog_content=Blog_content) \
                   ",
                   {
                   'bid':bid,
                   'blog_name':blog_name,
                   'blog_content':blog_content
                   }
                  )

	db.commit()
	db.close()
   