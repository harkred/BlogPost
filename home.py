from tkinter import *
import re
from tkinter import messagebox
from connections import write_register,result,login_results
import sqlite3

# Function to check password
def check_password():
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
                from browse import brew
                brew(user_detail[0], user_detail[1], user_detail[2], user_detail[3], root)
                break
    else:
        Username.delete(0,END)
        Password.delete(0,END)
        messagebox.showerror(title="Account Not Found", message="Username not found. Please create an account.")

# Function to register
def register():
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
    

# Login window's function
def home():
    global root, Username, Password, Email, RUsername, RPassword, CPassword

    # Creating the window
    root = Tk()
    root.title(" Login")
    root.resizable(0,0)

    # Frame for Login
    login_frame = LabelFrame(root,text=" Login ",font=('Consolas', 10), labelanchor=N,width=200,height=700)
    login_frame.grid(row=0,column=0,padx=30,pady=20,sticky=N)

    # Username Label and Entry
    Label(login_frame,text="Username: ",font=('Consolas', 10),padx=10,pady=5).grid(row=0,column=0)
    Username = Entry(login_frame,width=40,font=('Consolas', 10), borderwidth=4)
    Username.grid(row=0,column=1,padx=5,pady=2)

    # Password Label and Entry
    Label(login_frame,text="Password: ",font=('Consolas', 10),padx=10,pady=5).grid(row=1,column=0)
    Password = Entry(login_frame,width=40,font=('Consolas', 10), borderwidth=4)
    Password.grid(row=1,column=1,padx=5,pady=2)
    Password.config(show="•")

    # Button to Login and run check_password function
    Button(login_frame,text="Login",width=20,command=check_password,font=("Consolas",10)).grid(row=2,column=1,padx=5,pady=10)

    Label(root,text="Not a member? Signup now! ",font=('Consolas', 10),padx=10,pady=5).grid(row=1,column=0,sticky=N)

# ----------------------------------------------------------------------------------------------- #
    # Frame for Register
    register_frame = LabelFrame(root,text=" Register ", labelanchor=N,width=200,height=700)
    register_frame.grid(row=2,column=0,padx=30,pady=30)


    # Email Label and Entry
    Label(register_frame,text="Email:        ",font=('Consolas', 10),padx=10,pady=5).grid(row=0,column=0)
    Email = Entry(register_frame,width=40,font=('Consolas', 10), borderwidth=4)
    Email.grid(row=0,column=1,padx=5,pady=2)

    # Username Label and Entry
    Label(register_frame,text="Username:     ",font=('Consolas', 10),padx=10,pady=5).grid(row=1,column=0)
    RUsername = Entry(register_frame,width=40,font=('Consolas', 10), borderwidth=4)
    RUsername.grid(row=1,column=1,padx=5,pady=2)

    # Password Label and Entry
    Label(register_frame,text="Password:     ",font=('Consolas', 10),padx=10,pady=5).grid(row=2,column=0)
    RPassword = Entry(register_frame,width=40,font=('Consolas', 10), borderwidth=4)
    RPassword.grid(row=2,column=1,padx=5,pady=2)
    RPassword.config(show="•")

    # Confirm Password Label and Entry
    Label(register_frame,text="Confirm Password: ",font=('Consolas', 10),padx=10,pady=5).grid(row=3,column=0)
    CPassword = Entry(register_frame,width=40,font=('Consolas', 10), borderwidth=4)
    CPassword.grid(row=3,column=1,padx=5,pady=2)
    CPassword.config(show="•")

    # Button to Register and run register function
    Button(register_frame,text="Register",width=20,command=register,font=("Consolas",10)).grid(row=4,column=1,padx=5,pady=10)

    root.mainloop()