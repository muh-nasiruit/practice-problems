''' 7. Write a function that can calculate projectile motion.
'''

def m_projectile():
    v_i = float(input("Enter the initial velocity of projectile: "))
    ang = float(input("Enter the angle of releasing the projectile: "))
    g = 9.8
    from math import pi
    rad = pi * ang / 180
    #For time to reach its destination
    from math import sin
    t = (2 * v_i * sin(rad))/g
    print("The time the projectile takes to land is {:3.2f}s".format(t))
    #For range of the projectile
    rng = ((v_i**2) * sin(2 * rad)) / g
    print("The range of the projectile is {:3.2f}m".format(rng))

m_projectile()
