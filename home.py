from tkinter import *

def home():
    root = Tk()

    # Frames
    login_frame = LabelFrame(root,text=" Login ", labelanchor=N,width=200)
    login_frame.grid(row=0,column=0,padx=5,pady=10)
    Label(login_frame,text="Test").pack()

    register_frame = LabelFrame(root,text=" Register ", labelanchor=N,width=200)
    register_frame.grid(row=0,column=1,padx=5,pady=10)
    Label(register_frame,text="Test").pack()

    root.mainloop()   