from tkinter import *

def brow():
	browse = Tk()
	browse.geometry("1100x700")

	#Frames
	sidebar_frame = Frame(browse)
	sidebar_frame.pack(fill=Y, expand=1, side='left')

	mainloop()