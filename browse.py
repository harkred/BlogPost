from tkinter import *
from home import home

def blog():
	for child in main_frame.winfo_children():
		child.pack_forget()
	
	add_blog.config(state=DISABLED)
	
	BLOG = Label(main_frame, text='Blog')
	BLOG.pack(side='top')

	BLOG_NAME = Label(main_frame, text='Blog name: ')
	BLOG_NAME.pack(side='left')

	BLOG_DESC = Label(main_frame, text='Blog description: ')
	BLOG_DESC.pack(side='left', anchor=S)

	BLOG_CONT = Label(main_frame, text='Blog content: ')
	BLOG_CONT.pack(side='left', anchor=S) 

def brew():
	browse = Tk()
	browse.geometry("1100x700")

	#Frames
	sidebar_frame = Frame(browse)
	sidebar_frame.pack(fill=Y, expand=1, side='left', anchor=W)

	global add_blog
	add_blog = Button(sidebar_frame, text='Add Blog', command=blog)
	global log_out
	log_out = Button(sidebar_frame, text='Log out', command=home)

	add_blog.pack(anchor=NW)
	log_out.pack(anchor=W)

	global main_frame
	main_frame = Frame(browse)
	main_frame.pack(fill=BOTH, expand=1, side='right', anchor=E)

	mainloop()