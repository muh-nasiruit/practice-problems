'''Program 01
.
Creating a Program to show Label
'''

import tkinter
window = tkinter.Tk()
window.title('First Program')
tkinter.Label(window, text='its just a Label', fg='black', bg='red').pack()
window.mainloop()

'''Program 02

Creating a program to make Frames and Labels using pack
'''

import tkinter 
window=tkinter.Tk()
window.title('second program')
x_frame = tkinter.Frame(window).pack(side='top')
y_frame = tkinter.Frame(window).pack(side='bottom')

#if i redefine pack in Labels then upper value will be overwritten
#default pack side = top can be bottom,left,right as well

tkinterLabel


import tkinter
window=tkinter.Tk()
window.title('practice')
e1=tkinter.Entry(window).grid(row=0,column=1)
label=tkinter.Label(window,text='UserName:').grid(row=0,column=0)
window.mainloop()

def greetings():    
    label=tkinter.Label(window,text='Hello World').pack()

btn=tkinter.Button(window,text='Click Me',command=greetings).pack()

window.mainloop()



































