f = open('extra.txt')
str = f.read()
print(str)
f.close()

f = open('extra.txt')
i = f.read(5)
print(i)
f.close()



def stats():
    #wordcount
    f = open('extra.txt')
    strs = f.read()
    lst = strs.split()
    print('word count: ', len(lst))
    #linecount
    f = open('extra.txt')
    strs = f.readlines()
    print('line count: ', len(strs))
    #character count
    f = open('extra.txt')
    strs = f.readline()
    print('character count: ', len(strs))
stats()


f1 = open('extra.txt', 'w')
f1.write('This is the writing function file for zafir')
f1.close()

f2 = open('extra.txt', 'a')
f2.write('appended text in file')
f2.close()

def distribution():
    f = open('grades.txt', 'r')
    strs = f.read()
    lst = strs.split()
    num = [6, 2, 3, 2, 2, 4, 1, 2]
    for i in range(len(num)):
        print(num[i], 'students got', lst[i])
distribution()
    
def duplicate():
    f = open('grades.txt', 'r')
    strs = f.read()
    lst = strs.split()
    
    if len(lst) == len(set(lst)):
        return False
    else:
        return True
duplicate()

'''
 hint 4 
 read file
 check if 4 letter
 replace with 4 xxxx
 and then write the file into list
'''
def abc(name):
    pp = open(name,'rt')
    pw = open('abc.txt','w')
    for i in pp:
        w = i.split(' ')
        for word in w:
            if len(word) ==4:
                i = i.replace(word, 'xxxx')
        pw.write(i)
        print(i)
    pp.close()
    pw.close()
    
abc('grades.txt')
        
        
lst = []
for i in range(5):
    n = int(input("Enter a number: "))
    lst.append(n)

def firstneg(lst):
    for j in lst:
        if j < 0:
            print(lst.index(j))
        else:
            p = -1
            print(p)

firstneg(lst)
print(lst)
        
x=5        
a=lambda x: x**2
print(a(5))        
        
        

        
        
        
        
        
        
        


























