'''3. Write function even() that takes a positive integer n as input and prints on the screen all
numbers between, and including, 2 and n divisible by 2 or by 3, using this output format:
>>> even(17)
2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16,
'''

def even(n):
    if n >= 0: 
        for i in range(0,n):
            ev = i%2
            od = i%3
            if ev == 0 or od == 0:
                print(i, end=', ')
    return n
even(20)
        
