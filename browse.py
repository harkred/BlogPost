from tkinter import *
from home import home

def discar():
    for child in main_frame.winfo_children():
        child.pack_forget()
        child.place_forget()
        
    add_blog.config(state=NORMAL)
    
def submit():
    pass

def blog():
	for child in main_frame.winfo_children():
		child.pack_forget()
	
	add_blog.config(state=DISABLED)
    
	BLOG = Label(main_frame, text='Blog')
	BLOG.pack(side='top', pady=25)
    
	discard = Button(main_frame, text='Discard', command=discar)
	discard.pack(side='right', anchor=N, padx=100)
    
	BLOG_NAME = Label(main_frame, text='Blog name: ')
	BLOG_NAME.pack()
	BLOG_NAME.place(x=150, y=125)
    
	BLOG_CONT = Label(main_frame, text='Blog content: ')
	BLOG_CONT.pack()
	BLOG_CONT.place(x=150, y=170)

	blog_name = Entry(main_frame, width=100)
	blog_name.pack()
	blog_name.place(x=250, y=125)
    
	contscroll = Scrollbar(main_frame)
	contscroll.pack()
	contscroll.place(x=900, y=170)
    
	blog_cont = Text(main_frame, yscrollcommand=contscroll.set)
	blog_cont.pack()
	blog_cont.place(x=250, y=170)
    
	contscroll.config(command=blog_cont.yview)
    
	save_blog = Button(main_frame, text='Submit', command=submit)
	save_blog.pack()
	save_blog.place(x=475, y=570)
    
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