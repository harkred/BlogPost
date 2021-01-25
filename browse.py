from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from home import home
from PIL import ImageTk, Image
from connections import insert_blog, get_bloginfo, get_blog, get_ublog

#Main Frame window (Where everything starts after loggin in)_________________________
def _main_frame():
	global main_frame, left_frame, right_frame, menu, menu_text, blog_lst, result
    
	try: 
		main_frame.destroy()
        
	except Exception: 
		pass
        
    #Frames
	main_frame = ttk.LabelFrame(browse)
	main_frame.pack(fill=BOTH, expand=1)
    
	left_frame = ttk.LabelFrame(main_frame)
	left_frame.pack(fill=Y, expand=1, side=LEFT, anchor=W, ipadx=60)

	right_frame = ttk.LabelFrame(main_frame, text='Welcome Back {}'.format(USER))
	right_frame.pack(fill=BOTH, expand=1, side=RIGHT)

    #Menu for navigating through different frames
	menu_text = "_______\n_______\n_______"
    
	menu = ttk.Button(left_frame, text=menu_text, command=popup)
	menu.pack(anchor=NW, padx=5, pady=5)
    
    #Blogs to browse through
	blog_scroll = ttk.Scrollbar(right_frame)  

	blog_lst = Listbox(right_frame, width=400, yscrollcommand=blog_scroll.set, font=('Consolas', 15))

	blog_scroll.pack(side='right', fill=Y)

	blog_lst.pack(fill=BOTH, expand=1)

	blog_scroll.config(command=blog_lst.yview)
    
    #Where all the blogs get stored and then get added
	result = get_bloginfo()

	for data in result:
		blog_lst.insert(END, "{0:<65}@{1}".format(data[1],data[0]))

	blog_lst.bind('<Double 1>', content)

#Function to popdown the navigation buttons
def popdown():
    pop.destroy()
    menu.config(command=popup)

#Function to popup the navigation buttons    
def popup():
    global pop
    
    pop = ttk.LabelFrame(left_frame)
    pop.pack(side='left', anchor=NW)
    
    home = ttk.Button(pop, text='   Home   ', command=back_to_browse)
    
    add_blog = ttk.Button(pop, text=' Add Blog ', command=blog)
    
    your_blogs = ttk.Button(pop, text='Your Blogs', command=ublog)

    log_out = ttk.Button(pop, text=' Log out  ', command=logout)

    home.pack(ipadx=15, ipady=15, anchor=NW)
    add_blog.pack(ipadx=15, ipady=15, anchor=NW)
    your_blogs.pack(ipadx=15, ipady=15, anchor=NW)
    log_out.pack(ipadx=15, ipady=15, anchor=NW)
    
    menu.config(command=popdown)

#Function to return to the browse area
def back_to_browse():
    menu.config(text=menu_text, command=popup)
    _main_frame()

#Displays selected blog from browse area
def content(event):
    global bcon
    
    for child in right_frame.winfo_children():
        child.pack_forget()
    
    try: popdown()
    except Exception as e: pass
    
    #Getting blog algorithm
    a = blog_lst.get(ANCHOR)
    bname = a[0:65].strip()
    uname = a[(a.index('@')+1):]

    #Menu configuration to navigate to the browse
    menu.config(text='Back', command=back_to_browse)
    
    bcon = scrolledtext.ScrolledText(right_frame, width=300, font=('Consolas', 15))
    bcon.pack(fill=BOTH, expand=1)

    blog = get_blog(bname, uname)
    bcon.insert(1.0, blog[0][0])
    
    bcon.config(state=DISABLED)

#To navigate back to our blogs
def back_to_ublog():
    ubcon.pack_forget()
    menu.config(text=menu_text, command=popup)
    ublog()

#To see the content of our selected blogs
def ucontent(event):
    global ubcon
    
    popdown()
    
    for child in right_frame.winfo_children():
        child.pack_forget()
    
    ubname = ublog_lst.get(ANCHOR)
    
    menu.config(text='Back', command=back_to_ublog)
    
    right_frame.config(text=ublog_lst.get(ANCHOR))
    
    ubcon = scrolledtext.ScrolledText(right_frame, width=400, font=('Consolas', 15))
    ubcon.pack(fill=BOTH, expand=1)
    
    ublog = get_blog(ubname, USER)
    ubcon.insert(1.0, ublog[0][0])
    
    ubcon.config(state=DISABLED)

#For submitting blog
def submit():
    blgname = blog_name.get()
    if len(blog_name.get())>60:
        messagebox.showerror("","Blog Name cannot be longer than 60 characters.")
        return

    blgcont = blog_cont.get(1.0, END)
    valid = 0
    
    #To check the validity of content of the blog
    for char in blog_cont.get(1.0, END):
        if char.isdigit() or char.isalpha():
            valid = 1
            break
            
    if blog_name.get() != '' and valid == 1:
            messagebox.showinfo('', 'Blog added successfully')
            insert_blog(ID, blgname, blgcont)
            blog_name.delete(0, END)
            blog_cont.delete(1.0, END)
            brew(USER, PASSWD, EMAIL, ID)
        
    else:
        if blog_name.get() == '': messagebox.showerror('', 'Please fill the blog name field')
        if valid == 0: messagebox.showerror('', 'Please fill the blog content field')

#Frame which allows users to rite blogs
def blog():
	global blog_name, blog_cont

	popdown()

	for child in right_frame.winfo_children():
		child.pack_forget()
    
	right_frame.config(text='Let your thoughts flourish')
    
	blog_frame = ttk.LabelFrame(right_frame)
	blog_frame.pack(fill=BOTH, expand=1)
    
	BLOG = ttk.Label(blog_frame, text='Blog')
	BLOG.grid(row=0, column=0, columnspan=2, pady=10)
    
	BLOG_NAME = ttk.Label(blog_frame, text='Blog name: ')
	BLOG_NAME.grid(row=1, column=0, pady=20)
    
	BLOG_CONT = ttk.Label(blog_frame, text='Blog content: ')
	BLOG_CONT.grid(row=2, column=0, sticky=N, pady=20)

	blog_name = ttk.Entry(blog_frame, width=150)
	blog_name.grid(row=1, column=1, sticky=W)

	blog_cont = scrolledtext.ScrolledText(blog_frame, width=150, height=35, font=('Consolas', 10))
	blog_cont.grid(row=2, column=1, sticky=W)

	button_frame = ttk.LabelFrame(blog_frame)
	button_frame.grid(row=3, column=0, columnspan=2)

	save_blog = ttk.Button(button_frame, text='Submit', command=submit)
	save_blog.grid(row=0, column=0)
    
	discar_blog = ttk.Button(button_frame, text='Discard', command=back_to_browse)
	discar_blog.grid(row=0, column=1)

#Frame where one can browse throught their own submitted blogs
def ublog():
	global ublog_lst

	popdown()
    
	for child in right_frame.winfo_children():
		child.pack_forget()
    
	right_frame.config(text='YOUR BLOGS {}'.format(USER))
    
	ublog_scroll = ttk.Scrollbar(right_frame)  
	
	ublog_lst = Listbox(right_frame, width=400, yscrollcommand=ublog_scroll.set, font=('Consolas', 15))
	ublog_lst.bind('<Double 1>', ucontent)
    
	ublog_scroll.pack(side='right', fill=Y)
	
	ublog_lst.pack(fill=BOTH, expand=1)
  
	ublog_scroll.config(command=blog_lst.yview)
    
	res = get_ublog(ID)
    
	for udata in res:
		ublog_lst.insert(END, udata[0])

#Function to logout
def logout():
	browse.destroy()
	home()

#This is where our main window starts
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