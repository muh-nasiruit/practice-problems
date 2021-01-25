'''PF Lab after mid2

'''

languages = set()
language = {'C','C++','C'}
print(language)

language.add('C#')
print(language)

language.discard('Java')
print(language)

l = language.pop()
print(l)

'''alternative method for Q3
'''

dishes = set()
for i in range(3):
    a = input('Enter your dish: ')
    dishes.add(a)
print(dishes)
l = len(dishes)
print(l)

while (l != 0):
    n = dishes.pop()
    l = l - 1
print(n)

'''Programming Fundamentals Lab 10
'''

'''Programming Exercise 01
Write a program which will add your best five students name in a set. You will use a loop
to insert names in set.
'''

name = set()

for i in range(5):
    n = input('Enter the name: ')
    name.add(n)
print(name)

'''02
Write a program which will remove 2 friends who left UIT.
'''

for i in range(2):
    r = input('Enter student to be removed: ')
    name.remove(r)
print(name)

'''03
Write a program which will add your best dishes and then pop one by one until the set is
empty.
'''

dishes = set()
for i in range(4):
    u = input('Enter value: ')
    dishes.add(u)
print(dishes)


while len(dishes) != 0:
    b = dishes.pop()
    print(b)
    
    
print(dishes)

'''04
Write a program which will store number of items in a set after each purchasing the items
will be pop from the set and compare its price at the end program will give you the total
amount of items have been sold. Also find the max amount and minimum amount of items
sold.
'''

items = {'pen', 'pencil' ,'markers'}
lst = [['pen', 10],['pencil', 20],['markers', 30]]

f = []
final = 0
for i in range(0,2):
    a = input('Enter selected item: ')
    items.remove(a)
    f.append(a)
    break

    for j in range(len(f)):
        if a == lst[j][0]:
            final = final+lst[j][1]
print(final)

'''items={'pen','pencil','marker'}
lst=[['pen',10],['pencil',20],['marker',10]]
f = []
l=[]
final=0
for i in range(0,2):
    a=input("Enter selected items:")
    items.remove(a)
    f.append(a)
    for j in range(len(f)):
        if a==lst[j][0]:
            final=final+lst[j][1]
            l.append(lst[j][1])
            break

print(final)
print(max(l))'''

'''05
Write a program which will compare two sets, Set A and Set B. Both the sets have some students
who love to play one is hockey and other one is cricket. 10 of them play both. Now using sets find
how many of them are playing cricket only, if universal set is 40, students who play hockey are 21.
'''

#set a = hockey
#set b = cricket

set_a = {'21'}

#i = set_a.intersection(set_b)
i = {'10'}

#uni_set = set_a.union(set_b)
uni_set = {'40'}

set_b = uni_set.difference(set_a) 
print(set_b)





'''06
A pet store keeps track of the purchases of customers over a four-hour period. The store manager
classifies purchases as containing a dog product, a cat product, a fish product, or product
for a different kind of pet. She found.
a. 83 purchased a dog product
b. 101 purchased a cat product
c. 22 purchased a fish product
d. 31 purchased a dog and a cat product
e. 8 purchased a dog and a fish product
f. 10 purchased a cat and a fish product
g. 6 purchased a dog, a cat and a fish product
h. 34 purchased a product for a pet other than a dog, cat or a fish.
    i. How many purchases were for a dog product only?
    ii. How many purchases were for cat product only?
    iii. How many purchases for a dog or a fish product?
    iv. How many purchases were there in total?
'''


'''07
Solve the following problem of real world.
A camp of international students has 110 students, as shown in the diagram. The diagram will elaborate
that all the students speak some kind of a language. We need to find out how many that speak none of
them out of 110 students.
Find how many students speak
a. English and Spanish but not French?
b. Neither English, Spanish, nor French?
c. French, but neither English nor Spanish?
d. Only one of the three languages?
e. Exactly two of the three languages?
'''






l = {'C', 'C++', 'C#'}
l1 = {'Python', 'Java', 'C'}

d = l.intersection(l1) # l.difference(l1)
f = l-l1
print(d)     

f = l ^ l1 #symmetric differnece where intersection in subtacted out

#Q6 (verify)

u = l.union(l1)
print(u)


            















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    














































