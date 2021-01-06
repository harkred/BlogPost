from tkinter import *
from home import home

def blog():
	for child in main_frame.winfo_children():
		child.pack_forget()
	add_blog.config(state=DISABLED)
	BLOG = Label(main_frame, text='Blog')
	BLOG.pack(side='top')
	
		 

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