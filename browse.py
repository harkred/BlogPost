from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from home import home
from PIL import ImageTk, Image
from connections import insert_blog, get_bloginfo, get_blog, get_ublog

def _main_frame():
	global main_frame, left_frame, right_frame, menu, menu_text, blog_lst, result
    
	try: 
		main_frame.destroy()
        
	except Exception: 
		pass
        
    #Frames
    
	main_frame = LabelFrame(browse)
	main_frame.pack(fill=BOTH, expand=1)
    
	left_frame = LabelFrame(main_frame)
	left_frame.pack(fill=Y, expand=1, side=LEFT, anchor=W, ipadx=60)

	menu_text = "_______\n_______\n_______"
    
	menu = Button(left_frame, text=menu_text, command=popup, bg='#f7f7f7', font=('Consolas', 10))
	menu.pack(anchor=NW, padx=5, pady=5)

	right_frame = LabelFrame(main_frame, text='Welcome Back {}'.format(USER), font=('', 25))
	right_frame.pack(fill=BOTH, expand=1, side=RIGHT)

	blog_scroll = Scrollbar(right_frame)  

	blog_lst = Listbox(right_frame, width=400, yscrollcommand=blog_scroll.set, font=('Consolas', 15))

	blog_scroll.pack(side='right', fill=Y)

	blog_lst.pack(fill=BOTH, expand=1)

	blog_scroll.config(command=blog_lst.yview)

	result = get_bloginfo()

	for data in result:
		blog_lst.insert(END, '${}^'.format(data[1])+'                           @{}'.format(data[0]))

	blog_lst.bind('<Double 1>', content)

def back_to_browse():
    try:
        _main_frame()
        popdown()
    except Exception as e: pass

def content(event):
    for child in right_frame.winfo_children():
        child.pack_forget()
    
    a = blog_lst.get(ANCHOR)
    bname = a[(a.index('$')+1):a.index('^')]
    uname = a[(a.index('@')+1):]

    menu.config(text='Back', command=back_to_browse, font=('Consolas', 15))
    
    try: popdown()
    except Exception as e: pass
    
    bcon = scrolledtext.ScrolledText(right_frame, width=300, font=('Consolas', 15))
    bcon.pack(fill=BOTH, expand=1)

    blog = get_blog(bname, uname)
    bcon.insert(1.0, blog[0][0])
    
    bcon.config(state=DISABLED)

def back_to_ublog():
    ubcon.pack_forget()
    menu.config(text=menu_text, command=popup, font=('Consolas', 10))
    ublog()
    
def ucontent(event):
    global ubcon
    
    for child in right_frame.winfo_children():
        child.pack_forget()
    
    ubname = ublog_lst.get(ANCHOR)
    
    menu.config(text='Back', command=back_to_ublog, font=('Consolas', 15))
    
    right_frame.config(text=ublog_lst.get(ANCHOR))
    
    ubcon = scrolledtext.ScrolledText(right_frame, width=400, font=('Consolas', 15))
    ubcon.pack(fill=BOTH, expand=1)
    
    ublog = get_blog(ubname, USER)
    ubcon.insert(1.0, ublog)
    
    ubcon.config(state=DISABLED)
    
def submit():
    blgname = blog_name.get()
    blgcont = blog_cont.get(1.0, END)
    
    if len(blgname) != 0 and len(blgcont) !=0:
        insert_blog(ID, blgname, blgcont)
        blog_name.delete(0, END)
        blog_cont.delete(1.0, END)
        messagebox.showinfo('', 'Blog added successfully')
        brew(USER, PASSWD, EMAIL, ID)
        
    elif len(blgname) == 0 and len(blgcont) == 0: messagebox.showerror('', 'Please add the information properly')

def blog():
	global blog_name, blog_cont

	popdown()

	for child in right_frame.winfo_children():
		child.pack_forget()
    
	right_frame.config(text='Let your thoughts flourish')
    
	blog_frame = LabelFrame(right_frame)
	blog_frame.pack(fill=BOTH, expand=1)
    
	BLOG = Label(blog_frame, text='Blog', font=('Consolas', 20))
	BLOG.grid(row=0, column=0, columnspan=2, pady=10)
    
	BLOG_NAME = Label(blog_frame, text='Blog name: ', font=('Consolas', 10))
	BLOG_NAME.grid(row=1, column=0, pady=20)
    
	BLOG_CONT = Label(blog_frame, text='Blog content: ', font=('Consolas', 10))
	BLOG_CONT.grid(row=2, column=0, sticky=N, pady=20)

	blog_name = Entry(blog_frame, width=150, font=('Consolas', 10))
	blog_name.grid(row=1, column=1, sticky=W)

	blog_cont = scrolledtext.ScrolledText(blog_frame, width=150, height=35, font=('Consolas', 10))
	blog_cont.grid(row=2, column=1, sticky=W)

	button_frame = LabelFrame(blog_frame)
	button_frame.grid(row=3, column=0, columnspan=2)

	save_blog = Button(button_frame, text='Submit', command=submit, font=('Consolas', 10))
	save_blog.grid(row=0, column=0)
    
	discar_blog = Button(button_frame, text='Discard', command=back_to_browse, font=('Consolas', 10))
	discar_blog.grid(row=0, column=1)
    
def ublog():
	global ublog_lst

	popdown()
    
	for child in right_frame.winfo_children():
		child.pack_forget()
    
	right_frame.config(text='YOUR BLOGS {}'.format(USER), font=('Consolas', 25))
    
	ublog_scroll = Scrollbar(right_frame)  
	
	ublog_lst = Listbox(right_frame, width=400, yscrollcommand=ublog_scroll.set, font=('Consolas', 15))
	ublog_lst.bind('<Double 1>', ucontent)
    
	ublog_scroll.pack(side='right', fill=Y)
	
	ublog_lst.pack(fill=BOTH, expand=1)
  
	ublog_scroll.config(command=blog_lst.yview)
    
	res = get_ublog(ID)
    
	for udata in res:
		ublog_lst.insert(END, udata[0])

def logout():
	browse.destroy()
	home()

def popdown():
    pop.destroy()
    menu.config(command=popup)
    
def popup():
    global pop
    
    pop = LabelFrame(left_frame)
    pop.pack(side='left', anchor=NW)
    
    home = Button(pop, text='   Home   ', font=("Consolas",10), command=back_to_browse)
    
    add_blog = Button(pop, text=' Add Blog ', font=("Consolas",10), command=blog)
    
    your_blogs = Button(pop, text='Your Blogs', font=("Consolas",10), command=ublog)

    log_out = Button(pop, text=' Log out  ', font=("Consolas",10), command=logout)

    home.pack(ipadx=15, ipady=15, anchor=NW)
    add_blog.pack(ipadx=15, ipady=15, anchor=NW)
    your_blogs.pack(ipadx=15, ipady=15, anchor=NW)
    log_out.pack(ipadx=15, ipady=15, anchor=NW)
    
    menu.config(command=popdown)
    
def brew(username, passwd, email, oid):
	global browse, USER, PASSWD, EMAIL, ID
    
	USER = username
	PASSWD = passwd
	EMAIL = email
	ID = oid
    
	browse = Tk()
	browse.geometry("1350x750")
	browse.title(str(ID)+' '+USER)
	browse.state("zoomed")

	_main_frame()
    
	mainloop()