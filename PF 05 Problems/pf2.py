''' 2. Write two functions which will take required arguments for calculating the Area and Volume of
cylinder. Figure 2 is giving for your help.
'''

def rec_area():
    ln = float(input("Enter the length of the rectangle: "))
    bd = float(input("Enter the breadth of the rectangle: "))
    r_area = ln * bd
    deci_b1 = 2
    print("The area of the rectangle is {0:.{1}f}cm\u00b2".format(r_area, deci_b1))
 
def rec_volume():
    v_ln = float(input("Enter the length of the rectangle: "))
    v_bd = float(input("Enter the breadth of the rectangle: "))
    v_ht = float(input("Enter the height of the rectangle: "))
    r_vol = v_ln * v_bd * v_ht
    deci_b2 = 3
    print("The volume of the rectangle is {0:.{1}f}cm\u00b3".format(r_vol, deci_b2))
rec_area()
rec_volume()
    
