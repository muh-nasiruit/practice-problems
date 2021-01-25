#PF Lab 5

#Programming Exercise

''' 1. Write two functions which will take required arguments for calculating the Area and Volume of
cylinder. Figure 1 is giving for your help.
'''

def cyl_area():
    rad_a = float(input("Enter the radius of the cylinder: "))
    ht_a = float(input("Enter the height of the cylinder: "))
    from math import pi 
    deci_a1 = 2
    area = (2 * pi * rad_a * ht_a) + (2 * pi * rad_a**2)
    print("The area of the cylinder is {0:.{1}f}cm\u00b2".format(area, deci_a1))

def cyl_volume(): 
    rad_vol = float(input("Enter the radius of the cylinder: "))
    ht_vol = float(input("Enter the height of the cylinder: "))
    from math import pi 
    deci_a2 = 3
    vol = pi * rad_vol**2 * ht_vol
    print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(vol, deci_a2))
cyl_area()
cyl_volume()

