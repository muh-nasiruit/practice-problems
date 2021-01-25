'''7. Design an application in of small POS (Point of Sale) in which you generate burger type, quantity,
rate and amount line by line at the end it will print the total sum and 13 % GST. Keep in mind that
each receipt has username, and date of print. Create a function which can solve your problem.
'''
import time
print(time.strftime('%b/%d/%y\t\t\t\t%I:%M %p', time.localtime()))

print('\nUsername: Muhammad Nasir\n')
print('Burger\t\tType\tQuantity  Rate\tAmount')

f = []
f.append(['Fire House', 'Burger', 2, 350])
f.append(['Quadra', 'Burger', 1, 550])
f.append(['Drinks', 'Beverages', 3, 50])
f.append(['Oreo Shake', 'Smoothie', 4, 170])

def rpt(f):
    for i in f:
        print('# {:10}\t{:10}{:3}{:8} {:8}'.format(i[0], i[1], i[2], i[3], i[2]*i[3]))
    sub_t = 0    
    for j in range(len(f)):
        quantity = f[j][2]
        price = f[j][3]
        sub_t = sub_t + (price*quantity)
    gst = sub_t * (13/100)
    print()
    print('Sub Total:\t\t\t\tRs.{:4}'.format(sub_t))
    print('GST(13%):\t\t\t\tRs.{:3.4}'.format(gst))
    print('Net Bill:\t\t\t\tRs.{:4.5}'.format(sub_t + gst))
              
rpt(f)