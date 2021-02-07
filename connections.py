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

def get_bloginfo():
    db = sqlite3.connect('data.db')
    curse = db.cursor()
    
    curse.execute('SELECT Username, Blog_name FROM userdata, blog WHERE userdata.oid=blog.bid')
    result = curse.fetchall()
    
    db.commit()
    db.close()
    
    return result

def get_ublog(ID):
    db = sqlite3.connect('data.db')
    curse = db.cursor()
    
    curse.execute('SELECT Blog_name FROM blog WHERE BID = :BID', {'BID':ID})
    
    result = curse.fetchall()
    
    db.commit()
    db.close()
    
    return result
    
def get_blog(blog_name, username):
    db = sqlite3.connect('data.db')
    curse = db.cursor()
    
    curse.execute('SELECT Blog_content FROM userdata, blog WHERE Blog_name = :Blog_name AND userdata.Username = :Username', {'Blog_name':blog_name, 'Username':username})
    
    result = curse.fetchall()
    
    db.commit()
    db.close()
    
    return result    
   
def insert_blog(bid, blog_name, blog_content):
	db = sqlite3.connect('data.db')
	curse = db.cursor()

	curse.execute("INSERT INTO blog VALUES(:bid, :Blog_name, :Blog_content)",
                   {
                   'bid':bid,
                   'Blog_name':blog_name,
                   'Blog_content':blog_content
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
        
def update(username, password, email, oid, frame):
    
    data = result()
    
    usern_data = [user[0] for user in data]
    
    if len(password) >= 8 and username != '' and password != '':
        try:
            db = sqlite3.connect('data.db')
            curse = db.cursor()
            
            cmd = "UPDATE userdata SET \
                   username = :username, \
                   password = :password, \
                   email = :email \
                   WHERE oid = :oid"
            
            values = {'username':username, 'password':password, 'email':email, 'oid':oid}
            
            curse.execute(cmd, values)

            db.commit()
            db.close()
            messagebox.showinfo('', 'Account updated')
            
            frame()

        except Exception as e: messagebox.showerror('', 'Username already taken')
    
    if username == '' or email == '': messagebox.showerror('', 'Please fill the information')
    
    if len(password) < 8: messagebox.showerror('', 'Minimum length of password should be 8')
