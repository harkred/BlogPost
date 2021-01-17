from tkinter import *
from home import home
from PIL import ImageTk, Image
from connections import insert_blog, get_bloginfo, get_blog, get_ublog

def _main_frame():
	global browse, add_blog, main_frame, sidebar_frame, menu, USER, PASSWD, EMAIL, ID, blog_lst, result,pop
    
	try: 
		main_frame.destroy()
		sidebar_frame.destroy()
        
	except Exception: 
		pass
        
    #Frames
	sidebar_frame = Frame(browse)
	sidebar_frame.pack(fill=Y, side='left', anchor=W)
   
	#openimg = Image.open('menu_icon.jpg')
	#putimg = ImageTk.PhotoImage(openimg)

	menu = Button(sidebar_frame, text=' ', command=popup, bg='#f7f7f7')
	menu.pack(anchor=NW, padx=5, pady=5)

	main_frame = Frame(browse)
	main_frame.pack(fill=BOTH, side='right', anchor=E)
        
	WELCM = Label(main_frame, text='Welcome Back {}'.format(USER), font=('', 25))
	WELCM.pack(side='top')
        
	blog_scroll = Scrollbar(main_frame)  
       
	blog_lst = Listbox(main_frame, height=35, width=160, yscrollcommand=blog_scroll.set)
        
	blog_scroll.pack(side='right', fill=Y)
       
	blog_lst.pack(pady=15)
       
	blog_scroll.config(command=blog_lst.yview)
        
	result = get_bloginfo()
        
	for data in result:
		blog_lst.insert(END, '${}^'.format(data[1])+'                           @{}'.format(data[0]))
        
	blog_lst.bind('<Double 1>', content)

def back_to_browse():
    _main_frame()        

def content(event):
    global browse
    for child in main_frame.winfo_children():
        child.pack_forget()
    
    a = blog_lst.get(ANCHOR)
    bname = a[(a.index('$')+1):a.index('^')]
    uname = a[(a.index('@')+1):]

    back_btn = Button(main_frame, text='Back', command=back_to_browse)
    back_btn.pack(side='left', padx=20, anchor=N, ipadx=15, ipady=15)
    
    bscroll = Scrollbar(main_frame)
    bscroll.pack(fill=Y, side='right')
    
    bcon = Text(main_frame, yscrollcommand=bscroll.set)
    bcon.pack(fill=BOTH, expand=1, ipadx=100)
    
    bscroll.config(command=bcon.yview)
    blog = get_blog(bname, uname)
    bcon.insert(1.0, blog)
    
    bcon.config(state=DISABLED)

def back_to_ublog():
    ublog()
    
def ucontent(event):
    global browse, uback_btn
    for child in main_frame.winfo_children():
        child.pack_forget()
    
    ubname = ublog_lst.get(ANCHOR)

    uback_btn = Button(main_frame, text='Back', command=back_to_ublog)
    uback_btn.pack(side='left', padx=20, anchor=N, ipadx=15, ipady=15)
    
    ubscroll = Scrollbar(main_frame)
    ubscroll.pack(fill=Y, side='right')
    
    ubcon = Text(main_frame, yscrollcommand=ubscroll.set)
    ubcon.pack(fill=BOTH, expand=1, ipadx=100)
    
    ubscroll.config(command=ubcon.yview)
    ublog = get_blog(ubname, USER)
    ubcon.insert(1.0, ublog)
    
    ubcon.config(state=DISABLED)
    
def submit():
    global browse
    insert_blog(ID, blog_name.get(), blog_cont.get(1.0, END))
    blog_name.delete(0, END)
    blog_cont.delete(1.0, END)
    brew(USER, PASSWD, EMAIL, ID, browse)

def blog():
	global blog_name, blog_cont, browse

	popdown()

	for child in main_frame.winfo_children():
		child.pack_forget()
    
	BLOG = Label(main_frame, text='Blog')
	BLOG.pack(side='top', pady=25)
    
	BLOG_NAME = Label(main_frame, text='Blog name: ')
	BLOG_NAME.pack(anchor=NW, side=LEFT)
    
	BLOG_CONT = Label(main_frame, text='Blog content: ')
	BLOG_CONT.pack(anchor=W, side=LEFT)

	blog_name = Entry(main_frame, width=75)
	blog_name.pack(anchor=N, pady=5)

	Text_frame = Frame(main_frame)
	Text_frame.pack(anchor=E,padx=5)
    
	contscroll = Scrollbar(Text_frame)
	contscroll.pack(side=RIGHT,fill=Y)

	blog_cont = Text(Text_frame, yscrollcommand=contscroll.set)
	blog_cont.pack(anchor=S, pady=5)
	
	contscroll.config(command=blog_cont.yview)
    
	save_blog = Button(main_frame, text='Submit', command=submit)
	save_blog.pack()
    
	discar_blog = Button(main_frame, text='Discard', command=back_to_browse)
	discar_blog.pack()
    
def ublog():
	global ublog_lst

	popdown()
	for child in main_frame.winfo_children():
		child.pack_forget()
    
	URBLOGS = Label(main_frame, text='YOUR BLOGS {}'.format(USER), font=('Consolas', 25))
	URBLOGS.pack(side='top')
    
	ublog_scroll = Scrollbar(main_frame)  
	
	ublog_lst = Listbox(main_frame, height=35, width=160, yscrollcommand=ublog_scroll.set)
	ublog_lst.bind('<Double 1>', ucontent)
    
	ublog_scroll.pack(side='right', fill=Y)
	
	ublog_lst.pack(pady=15)
  
	ublog_scroll.config(command=blog_lst.yview)
    
	res = get_ublog(ID)
    
	for udata in res:
		ublog_lst.insert(END, udata[0])

def logout():
	browse.destroy()
	home()

def popdown():
    global pop
    pop.destroy()
    menu.config(command=popup)
    
def popup():
    global pop, add_blog, browse
    pop = Frame(browse)
    pop.pack(fill=Y, side='left', anchor=W)
    
    home = Button(pop, text='   Home   ', font=("Consolas",10), command=back_to_browse)
    
    add_blog = Button(pop, text=' Add Blog ', font=("Consolas",10), command=blog)
    
    your_blogs = Button(pop, text='Your Blogs', font=("Consolas",10), command=ublog)

    log_out = Button(pop, text=' Log out  ', font=("Consolas",10), command=logout)

    home.pack(ipadx=15, ipady=15)
    add_blog.pack(ipadx=15, ipady=15)
    your_blogs.pack(ipadx=15, ipady=15)
    log_out.pack(ipadx=15, ipady=15)
    
    menu.config(command=popdown)
    
def brew(username, passwd, email, oid):
	global browse, add_blog, main_frame, sidebar_frame, menu, USER, PASSWD, EMAIL, ID, blog_lst, result,pop
    
	USER = username
	PASSWD = passwd
	EMAIL = email
	ID = oid
    
	browse = Tk()
	browse.geometry("1200x700")
	browse.title(str(ID)+' '+USER)

	_main_frame()
    
	mainloop()