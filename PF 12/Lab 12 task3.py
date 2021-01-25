'''
Task 3


1. re.match()
2. re.search()
3. re.findall()
4. re.split()
5. re.sub()
6. re.compile()

'''


import tkinter
import re

window = tkinter.Tk()
window.title('Lab 12')

e1 = tkinter.Entry(window, width=20, borderwidth=10, bg='grey')
e2 = tkinter.Entry(window, width=20, borderwidth=10, bg='grey')

e1.pack()   
e2.pack()

      
             
def get1():
    z1 = e1.get()
    z2 = e2.get()
    if re.match(z1,z2): 
        tkinter.Label(window, text = 'Found').pack()
    else:
        tkinter.Label(window, text = 'Not Found').pack()



def get2():
    z1 = e1.get()
    pat = '[\w\._-]+@[\w\.-]'
    if re.search(pat, z1):
        a = tkinter.Label(window, text = 'Found').pack()
        f = open('result.txt', 'w')
        f.write('Found')
        f.close()
        print(a)
        
    else:
        b = tkinter.Label(window, text = 'NotFound').pack()
        f = open('result.txt', 'w')
        f.write('Not Found')
        f.close()
        print(a)
        


def get3():
    z1 = e1.get()
    z2 = e2.get()
    x = re.findall(z2, z1)
    if x == []:
        tkinter.Label(window, text = 'Not Found').pack()
    else:
        tkinter.Label(window, text = 'found').pack()
       
        
        
    
def get4():
    z1 = e1.get()
    z2 = e2.get()
    
    s = re.split(z2, z1)
    tkinter.Label(window, text = s).pack()
    print(s) 
    

def get5():
    z1 = e1.get()
    pp = re.sub('\s', 'LMAOLMAOLMAO', z1,4)
    print(re.sub('\s', 'lmaolmaolmao', z1,4))
    tkinter.Label(window, text = pp).pack()
    
def get6():
    z1 = e1.get()
    z2 = e2.get()
    ab = re.compile(z2)
    if ab.match(z1):
        print('Found')
        tkinter.Label(window, text = 'Found').pack()
    else:
        print('Not Found')
        tkinter.Label(window, text = 'Not Found').pack()
    


tkinter.Button(window, text="Match", command=get1).pack()
tkinter.Button(window, text="Search", command=get2).pack()
tkinter.Button(window, text="Find", command=get3).pack()
tkinter.Button(window, text="Split", command=get4).pack()
tkinter.Button(window, text="Sub", command=get5).pack()
tkinter.Button(window, text="Compile", command=get6).pack()

window.mainloop()































