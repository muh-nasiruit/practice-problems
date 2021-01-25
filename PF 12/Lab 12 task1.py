
'''a. choice()
b. randrange(beg, end, step)
c. random()
d. seed()
e. shuffle()
f. uniform

'''


import random


#it provides a random no. from the given set of nunbers
print(random.choice([1,2,3,4,5,6])) 



#it provides a random number from 0 to 1
print(random.random())

#it gives a random number from the range defined by the user 
print(random.randrange(1, 52, 4))

#shuffle exchanges the elements randomly in a list
lst = [2, 3, 4, 5]
random.shuffle(lst)
print(lst)

#it uses a constantly changing number i.e system time to get a random n
print(random.seed())
print(random.random())

'''it gives a random number according to a preset formula
formula = a + (b-a) * random() 
'''

print(random.uniform(1, 100))















