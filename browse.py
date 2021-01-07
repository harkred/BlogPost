from tkinter import *
from home import home
from PIL import ImageTk, Image

def discar():
    for child in main_frame.winfo_children():
        child.pack_forget()
        child.place_forget()
        
    add_blog.config(state=NORMAL)
    menu.config(state=NORMAL)
    
def submit():
    pass

def blog():
	for child in main_frame.winfo_children():
		child.pack_forget()
	
	add_blog.config(state=DISABLED)
	menu.config(state=DISABLED)
    
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
	browse.destroy()
	home()

def popdown():
    global pop, add_blog
    pop.destroy()
    add_blog.destroy()
    menu.config(command=popup)
    
def popup():
    global pop, add_blog
    pop = Frame(browse)
    pop.pack(fill=Y, side='left', anchor=W)
    
    add_blog = Button(pop, text='Add Blog', command=blog)

    log_out = Button(pop, text='Log out', command=logout)

    add_blog.pack()
    log_out.pack()
    
    menu.config(command=popdown)
    
def brew():
	global browse, add_blog, main_frame, sidebar_frame, menu

	browse = Tk()
	browse.geometry("1100x700")

	#Frames
	sidebar_frame = Frame(browse)
	sidebar_frame.pack(fill=Y, side='left', anchor=W)
    
	openimg=Image.open('menu_icon.jpg')
	putimg=ImageTk.PhotoImage(openimg)
	menu = Button(sidebar_frame, text=' ', command=popup, image=putimg, bg='white')
	menu.pack(anchor=NW, ipadx=10, ipady=5, padx=5, pady=5)

	main_frame = Frame(browse)
	main_frame.pack(fill=BOTH, expand=1, side='right', anchor=E)

	mainloop()