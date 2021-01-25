
out = []
for i in range(1,11):
    out.append(i)
print(out)


#via list comprehension

final = [i for i in range (1,11)]
print(final)

final = [ i**2 for i in range(1,11) if i%2==0]
print(final)

matrix = [[1,2],[3,4]]

for i in range(0,2):
    for j in range(0,2):
        print(matrix[i][j], end = '\t')
    print('\n')
    
final = [[matrix[i][j] for j in range(0,2)] for i in range(0,2)]
print(final)

#Programming Exercise 1

out = [i for i in range(1,144) if i%12==0]
print(out)

#Programming Exercise 2

lst = [1, -2, 3, -4, 5, -6]

pos, neg = [i for i in lst if i>0 ], [i for i in lst if i<0]
print(pos, neg)

#Programming Exercise 3 

final = { i:j for i in range(1,101) for j in range(1,101) if j>5 and j%7==0 and j%2==0}
print(final)

#Programming Exercise 4

d = {1: 'a', 2: 'b', 3:'c'}

d_out = {i*2:j*2 +'a' for i, j in d.items()}

print(d_out)


nest = {1:{'a' : 2},
        2:{'b' : 3},
        3:{'c' : 4},
        }

#for outer keys
#f = {k1:{ } for (k1,v1) in nest.items()}
f = {k1:{k2 for (k2,v2) in v1.items() } for (k1,v1) in nest.items()}
print(f)

#Programming Exercuise 5

'''Built-in Functions in Python for Lambda

filter(): requires 2 parameters; a function to define the filtering 
and any iterator like lists,tuples etc.

It is used to select some particular elements from a sequence of elements.

Example:
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = filter (lambda x: x > 4, sequences) 
print(list(filtered_result))
[OUT]: [10, 8, 7, 5, 11]


map(): requires 2 parameters; a function that defines the operation,
one or more iterators/sequences/lists/tuples

It is used to apply a particular operation to every element in a sequence

Example: 
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = filter (lambda x: x > 4, sequences) 
print(list(filtered_result))
[OUT]: [100, 4, 64, 49, 25, 16, 121, 0, 1]

reduce(): reduce is similar to map() as it applies an operation on every element 
in a sequence but differs in working.
    
It takes 2 parameters; a function that defines the operation, a sequence

Working: 
    It performs the operation on the first 2 elements of the sequence and then
    takes the result of that to operate on the next element

Example:
from functools import reduce
sequences = [1,2,3,4,5]
product = reduce (lambda x, y: x*y, sequences)
print(product)
[OUT]: 120


'''




#Programming Exercise 6

def table(n):
    return lambda a:a*n;
 
n = int(input("Enter the number: ")) 
b = table(n) 
for i in range(1,11):
    print(n,"x",i,"=",b(i));
    
table(4)

#lambda functions
#anonymous functions

def square(n):
    res=n*n
    return res

square(2)

final = lambda n,x: n*n*x
print(final(2,3))





















