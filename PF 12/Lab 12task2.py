import tkinter
import random


window = tkinter.Tk()
window.title('Dice Game')

def ludo1():
    z = random.choice([1, 2, 3, 4, 5, 6])
    tkinter.Label(window, text = z).pack()
    
def ludo2():
    w = random.choice([1, 2, 3, 4, 5, 6])
    tkinter.Label(window, text = w).pack()


tkinter.Button(window, text="single", command=ludo1).pack()
tkinter.Button(window, text="double", command=ludo2).pack()


window.mainloop()








































