'''6. Write multiple functions that can calculate three laws of motions in physics
'''
def law_1():
    #To find the final velocity
    v_i1 = int(input("Enter the initial velocity: "))
    a1 = int(input("Enter the acceleration: "))
    t1 = int(input("Enter the time elapsed in sec: "))
    v_f1 = v_i1 + (a1 * t1)
    print("The final velocity is {}m/s".format(v_f1))

def law_2():
    #To find the distance
    v_i2 = float(input("Enter the initial velocity: "))
    a2 = float(input("Enter the acceleration: "))
    t2 = float(input("Enter the time elasped: "))
    dst = (v_i2 * t2) + (0.5*a2)*(t2)**2
    print("The distance calculated is {}m".format(dst))

def law_3():
    #To find the final velocity
    v_i3 = int(input("Enter the initial velocity: "))
    a3 = int(input("Enter the acceleration: "))
    dst2 = int(input("Enter the distance covered: "))
    from math import sqrt
    v_f2 = sqrt((v_i3)**2 + 2*(a3)*(dst2))
    print("The final velocity is {}m/s".format(v_f2))

law_1()
law_2()
law_3()
    
