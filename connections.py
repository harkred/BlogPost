import sqlite3
from tkinter import messagebox
from tkinter import *

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

	return results

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
   
def login_results(username):
	db = sqlite3.connect('data.db')
	cursor = db.cursor()

	cursor.execute(f"SELECT *, oid FROM userdata where Username = \"{username}\"")
	results = cursor.fetchall()

	db.commit()
	db.close()

	return results[0]

def write_register(username,password,cpassword,email):
	try:
		db = sqlite3.connect('data.db')
		cursor = db.cursor()

		cursor.execute(f"INSERT INTO userdata VALUES(\"{username.get()}\",\"{password.get()}\",\"{email.get()}\")")
		db.commit()
		db.close()
		messagebox.showinfo(title="Success!",message="Account created successfully.")
		email.delete(0,END)
		username.delete(0,END)
		password.delete(0,END)
		cpassword.delete(0,END)
	except Exception:
		messagebox.showerror(title="Error",message="Username Already exists. Please use some other username.")
		username.delete(0,END)
		password.delete(0,END)
		cpassword.delete(0,END)