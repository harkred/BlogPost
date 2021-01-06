from tkinter import *
from home import home

def blog():
	for child in main_frame.winfo_children():
		child.pack_forget()
	
	add_blog.config(state=DISABLED)
	BLOG = Label(main_frame, text='Blog')
	BLOG.pack(side='top')

	BLOG_NAME = Label(main_frame, text='Blog name: ')
	BLOG_NAME.pack(side='left', anchor=W, pady=5)

	BLOG_DESC = Label(main_frame, text='Blog description: ')
	BLOG_DESC.pack(side='left', anchor=W, pady=5)

	BLOG_CONT = Label(main_frame, text='Blog content: ')
	BLOG_CONT.pack(side='left', anchor=W, pady=5) 

def logout():
	global browse
	browse.destroy()
	home()

def brew():
	global browse, add_blog, main_frame

	browse = Tk()
	browse.geometry("1100x700")

	#Frames
	sidebar_frame = Frame(browse)
	sidebar_frame.pack(fill=Y, side='left', anchor=W)

	add_blog = Button(sidebar_frame, text='Add Blog', command=blog)

	log_out = Button(sidebar_frame, text='Log out', command=logout)

	add_blog.pack(anchor=NW)
	log_out.pack(anchor=W)

	main_frame = Frame(browse)
	main_frame.pack(fill=BOTH, expand=1, side='right', anchor=E)

	mainloop()