'''8. Create a function which will take a start point and end point from user and convert the numbers
in binary, octal, decimal, and hexa-decimal with proper formatting style.
The first line will be headings and the rest of the line with proper space between each type.
'''

def num_cov(i, f):
    n = ['Decimal', 'Binary', 'Octal', 'Hexa-decimal']
    print('{:8} {:8} {:8} {:8}'.format(n[0], n[1], n[2], n[3]))
    for j in range(i, f):
        print('{:8} {:8b} {:8o} {:8X}'.format(j, j, j, j))
num_cov(1,16)
        

