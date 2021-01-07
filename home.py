from tkinter import *

# Function to check password
def check_password():
    pass

# Function to register
def register():
    pass

# Login window's function
def home():

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

    # Frame for Register
    register_frame = LabelFrame(root,text=" Register ", labelanchor=N,width=200,height=700)
    register_frame.grid(row=2,column=0,padx=30,pady=30)


    # Email Label and Entry
    Label(register_frame,text="Email:        ",font=('Consolas', 10),padx=10,pady=5).grid(row=0,column=0)
    Email = Entry(register_frame,width=40,font=('Consolas', 10), borderwidth=4)
    Email.grid(row=0,column=1,padx=5,pady=2)

    # Username Label and Entry
    Label(register_frame,text="Username:     ",font=('Consolas', 10),padx=10,pady=5).grid(row=1,column=0)
    Username = Entry(register_frame,width=40,font=('Consolas', 10), borderwidth=4)
    Username.grid(row=1,column=1,padx=5,pady=2)

    # Password Label and Entry
    Label(register_frame,text="Password:     ",font=('Consolas', 10),padx=10,pady=5).grid(row=2,column=0)
    Password = Entry(register_frame,width=40,font=('Consolas', 10), borderwidth=4)
    Password.grid(row=2,column=1,padx=5,pady=2)
    Password.config(show="•")

    # Confirm Password Label and Entry
    Label(register_frame,text="Confirm Password: ",font=('Consolas', 10),padx=10,pady=5).grid(row=3,column=0)
    CPassword = Entry(register_frame,width=40,font=('Consolas', 10), borderwidth=4)
    CPassword.grid(row=3,column=1,padx=5,pady=2)
    CPassword.config(show="•")

    # Button to Register and run register function
    Button(register_frame,text="Register",width=20,command=register,font=("Consolas",10)).grid(row=4,column=1,padx=5,pady=10)

    root.mainloop()
