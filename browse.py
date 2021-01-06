from tkinter import *

browse = Tk()
browse.geometry("1100x700")

#Frames
sidebar_frame = Frame(browse)
sidebar_frame.pack(fill=Y, expand=1, side='left', anchor=W)

Button(sidebar_frame, text='Add Blog').pack(anchor=NW)
Button(sidebar_frame, text='Log out').pack(anchor=W)

main_frame = Frame(browse)
main_frame.pack(fill=BOTH, expand=1, side='right', anchor=E)

mainloop()