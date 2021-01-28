from tkinter import *
from home import home
import sqlite3
from connections import create_table_userdata, create_table_blog
try:
    create_table_userdata()
    create_table_blog()
    
except Exception as e: pass

home()