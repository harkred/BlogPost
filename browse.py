from tkinter import *

browse = Tk()
browse.geometry("1100x700")

#Frames
sidebar_frame = Frame(browse)
sidebar_frame.pack(fill=Y, expand=1, side='left')

Button(sidebar_frame, text='Add Blog').pack(side='left')
Button(sidebar_frame, text='Log out').pack(side='left')

mainloop()