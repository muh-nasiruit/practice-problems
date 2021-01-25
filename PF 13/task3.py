
'''Programming Exercise 
Task 3
'''

import tkinter
import sqlite3
from sqlite3 import Error


def connect():
    
    try:
        con = sqlite3.connect('test_database.db')
        print('connected')
    except Error:
        print(Error)
    finally:
        print('done')
        return con
    
con = connect()


def insert_data(con):
    c = con.cursor()
    
    print('inserted')
    window = tkinter.Tk()
    window.title("Database")
    i=c.execute('select * from book_table')
    for j in i:
        print(j)    
        
        tkinter.Label(window, text = j).pack()   

        window.mainloop()

insert_data(con)


'''
import tkinter as tk
from tkinter.messagebox import showinfo
import sqlite3

def insert_data() :

       db = sqlite3.connect("test_database.db")
       cur=db.cursor()
       cur.execute("INSERT INTO book_table VALUES (1, 'nasir', 'uit', 1999, 2000, 450, 'Yes')")
       print("Entry Added To Database")
       db.commit()
       showinfo( title = "Database", message = "Data in GUI")

class Myproj(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}


    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()





app = Myproj()
app.mainloop()
'''












