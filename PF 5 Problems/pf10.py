''' 10. Write a function which will generate a table of sin(), cos(), tan() with user defined range.
'''
def ang_table():
    i_val = int(input("Enter the final angle: "))
    f_val = int(input("Enter the initial angle: "))
    for i in range(i_val, f_val):
        import math
        rad_i = math.pi * i_val / 180
        rad_f = math.pi * f_val / 180
        print("sin {:3.2f} cos {:3.2f} tan {:3.2f}".format(math.sin(math.radians(i)), math.cos(math.radians(i)), math.tan(math.radians(i))))
ang_table()

