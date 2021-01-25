

from tkinter import *
import math
# creating basic window
window = Tk()
window.geometry("400x400") # size of the window width:- 500, height:- 375
window.resizable(0, 0) # this prevents from resizing the window
window.title("Scientific Calculator")



# 'btn_click' function continuously updates the input field whenever you enters a number
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 'btn_clear' function clears the input field
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

# 'btn_equal' calculates the expression present in input field
def btn_equal():
    global expression
    result = str(eval(expression)) # 'eval' function evalutes the string expression directly
    # you can also implement your own function to evalute the expression istead of 'eval' function
    input_text.set(result)
    expression = ""

expression = ""
# 'StringVar()' is used to get the instance of input field
input_text = StringVar()

# creating a frame for the input field
input_frame = Frame(window, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", 
                    highlightthickness = 1)
input_frame.pack(side = TOP)

# creating a input field inside the 'Frame'
input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", 
                    bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10) # 'ipady' is internal padding to increase the height of input field
# creating another 'Frame' for the button below the 'input_frame'
btns_frame = Frame(window, width = 312, height = 272.5, bg = "grey")
btns_frame.pack()

# first row
clear = Button(btns_frame, text = "C", fg = "black", width = 32,  height = 3, bd = 0, bg = "#eee", cursor = "hand2", 
               command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", 
                command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

# second row
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", 
               command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", 
               command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", 
              command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "X", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", 
                  command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

# third row
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", 
              command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", 
              command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", 
             command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", 
               command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

# fourth row
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", 
             command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", 
             command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", 
               command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", 
              command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

# fourth row
sin = Button(btns_frame, text = "sin", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", 
              command = lambda: btn_click(math.sin)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
cos = Button(btns_frame, text = "cos", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", 
               command = lambda: btn_click(math.cos)).grid(row = 4, column = 2, padx = 1, pady = 1)
tan = Button(btns_frame, text = "tan", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", 
                command = lambda: btn_click(math.tan)).grid(row = 4, column = 3, padx = 1, pady = 1)

# fifth row
zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", 
              command = lambda: btn_click(0)).grid(row = 5, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", 
               command = lambda: btn_click(".")).grid(row = 5, column = 2, padx = 1, pady = 1)
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", 
                command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)

window.mainloop()

'''

'''

import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("Receipt")
window.configure(background="grey")
tkinter.Label(window, text = 'Subway POS', relief = "raise", height = 2, width = 15, font =('Corbel' ,12, 'bold')).pack()

def POS_system(username, burger, quantity, cost):
    import time
    
    time = time.strftime('%A %b/%d/%y', time.localtime())
    if burger == 'Chicken':
        burger == 'Chicken'
    else:
        burger = 'Beef'
    
    amount = cost*quantity
    gst = '13% G.S.T'
    sum_total = (amount*13/100)+amount
    tkinter.Label(window, text = time, bg = "grey").pack()
    tkinter.Label(window, text = ("Username: {}\nBurger Type: {}\nQuantity: {}\nCost: {}\nSub Total: {}\nTax Applied: {}").format(username, burger,quantity,cost,amount,gst)).pack()
    tkinter.Label(window, text = "Total: {}".format(sum_total), bg = "lightgreen").pack()

tkinter.Button(window, command = POS_system, text = 'Print Receipt', height = 1, width = 10).pack(side = BOTTOM)

POS_system("Nasir", "Chicken", 2, 550)
window.mainloop()


'''

import tkinter as tk



def order_book(productName,productQuantity):
   print(productPrice * productQuantity)


def print_receipt():
   print(Receipt)


master = tk.Tk()
Receipt = "This is a Receipt"
stationary = {1:{'pencil' : '10'},
                           2:{'eraser': '20'} }

tk.Label(master,text='Welcome To Stationary Shop').pack()
tk.Label(master,text=stationary).pack()

productName= tk.Entry(master)
productQuantity = tk.Entry(master)
productName.pack()
productQuantity = tk.Entry(master)
productPrice = tk.Entry(master)
productPrice.pack()
tk.Button(master, text='Order', command=order_book(productName,productQuantity)).pack()
tk.Button(master, text='Print Receipt', command=print_receipt).pack()
master.mainloop()





'''









