from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import sqlite3
import re

from connections import write_register,result,login_results

# Function to check password
def check_password(event):
    global Username,Password
    records = result()
    for user in records:
        if user[0] == Username.get():
            if user[1] != Password.get():
                Password.delete(0,END)
                messagebox.showerror(title="Incorrect Password", message="The password entered is incorrect.")
                break
            else:
                user_detail = login_results(Username.get())
                Username.delete(0,END)
                Password.delete(0,END)
                root.destroy()
                from browse import brew
                brew(user_detail[0], user_detail[1], user_detail[2], user_detail[3])
                break
    else:
        Username.delete(0,END)
        Password.delete(0,END)
        messagebox.showerror(title="Account Not Found", message="Username not found. Please create an account.")

# Function to register
def register(event):
    global Email, RUsername, RPassword, CPassword
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    # pass the regular expression and the string in search() method 
    if not (re.search(regex,Email.get())):
        Email.delete(0,END)
        messagebox.showerror(title="Invalid Email",message="The Email Entered is invalid. Please try again.")
        return
    if len(RPassword.get()) < 8:
        RPassword.delete(0,END)
        CPassword.delete(0,END)
        messagebox.showerror(title="Password Error",message="The password must contain minimum 8 characters.")
        return
    if RPassword.get() != CPassword.get():
        RPassword.delete(0,END)
        CPassword.delete(0,END)
        messagebox.showerror(title="Password Error",message="Make sure that confirm password and password are same.")
        return
    write_register(RUsername,RPassword,CPassword,Email)

# Function to show/hide password
def show():
    global Password, Checked
    if Checked.get():
        Password.config(show="")
    else:
        Password.config(show="•")
    
# ----------------------------------------------------------------------------------------------- #
# Login window's function
def home():
    global root, Username, Password, Email, RUsername, RPassword, CPassword, Checked

    # Creating the window
    root = Tk()
    root.title(" Login")
    root.resizable(0,0)

    # Frame for Login
    login_frame = LabelFrame(root,text=" Login ", labelanchor=N,width=200,height=700)
    login_frame.grid(row=0,column=0,padx=30,pady=20,sticky=N)

    # Username Label and Entry
    Label(login_frame,text="Username: ",padx=10,pady=5).grid(row=0,column=0)
    Username = ttk.Entry(login_frame,width=40)
    Username.grid(row=0,column=1,padx=5,pady=2)
    Username.bind('<Return>', lambda e: Password.focus_set())

    # Password Label and Entry
    Label(login_frame,text="Password: ",padx=10,pady=5).grid(row=1,column=0)
    Password = ttk.Entry(login_frame,width=40, show="•")
    Password.grid(row=1,column=1,padx=5,pady=2, sticky = W)
    Password.bind('<Return>', check_password)

    # Show Password? Checkbox
    Checked = IntVar()
    Show_Password = ttk.Checkbutton(login_frame,text="Show Password", variable=Checked, command=show)
    Show_Password.grid(row=2,column=1)

    # Button to Login and run check_password function
    Login_Button = ttk.Button(login_frame,text="Login",width=20)
    Login_Button.grid(row=3,column=1,padx=5,pady=10)
    Login_Button.bind('<Button-1>', check_password)

    Label(root,text="Not a member? Signup now! ",padx=10,pady=5).grid(row=1,column=0,sticky=N)

# ----------------------------------------------------------------------------------------------- #
    # Frame for Register
    register_frame = LabelFrame(root,text=" Register ", labelanchor=N,width=200,height=700)
    register_frame.grid(row=2,column=0,padx=30,pady=30)


    # Email Label and Entry
    Label(register_frame,text="Email:        ",padx=10,pady=5).grid(row=0,column=0)
    Email = ttk.Entry(register_frame,width=40)
    Email.grid(row=0,column=1,padx=5,pady=2)
    Email.bind('<Return>', lambda e: RUsername.focus_set())

    # Username Label and Entry
    Label(register_frame,text="Username:     ",padx=10,pady=5).grid(row=1,column=0)
    RUsername = ttk.Entry(register_frame,width=40)
    RUsername.grid(row=1,column=1,padx=5,pady=2)
    RUsername.bind('<Return>', lambda e: RPassword.focus_set())

    # Password Label and Entry
    Label(register_frame,text="Password:     ",padx=10,pady=5).grid(row=2,column=0)
    RPassword = ttk.Entry(register_frame,width=40)
    RPassword.grid(row=2,column=1,padx=5,pady=2)
    RPassword.config(show="•")
    RPassword.bind('<Return>', lambda e: CPassword.focus_set())

    # Confirm Password Label and Entry
    Label(register_frame,text="Confirm Password: ",padx=10,pady=5).grid(row=3,column=0)
    CPassword = ttk.Entry(register_frame,width=40)
    CPassword.grid(row=3,column=1,padx=5,pady=2)
    CPassword.config(show="•")
    CPassword.bind('<Return>', check_password)

    # Button to Register and run register function
    Register_Button = ttk.Button(register_frame,text="Register",width=20,command=register)
    Register_Button.grid(row=4,column=1,padx=5,pady=10)
    Register_Button.bind('<Button-1>', check_password)

    root.mainloop()