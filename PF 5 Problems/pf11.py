''' 11. For a given semi-circle of 14 cm diameter two small semi-circle are inserted in it. Find the
area of perimeter including semi-circle and excluding semi-circle. Also find the area it covered
with two semi-circles and excluding two semi-circles.
'''
s_c1 = 14
s_c2 = 7
import math
peri_1 = math.pi * s_c1
peri_2 = math.pi * s_c2
area_1 = math.pi * (s_c1/2)**2
area_2 = math.pi * (s_c2/2)**2
deci = 2

#Area of perimeter including semi circle:
print("The area of perimeter including a semi circle is {0:.{1}f}cm\u00b2".format(area_1, deci))

#Area of perimeter excluding semi circle:
ex_1 = area_1 - area_2
print("The area of perimeter excluding a semi circle is {0:.{1}f}cm\u00b2".format(ex_1, deci))

#Area of perimeter including two semi circles:
print("The area of perimeter including two semi circles is {0:.{1}f}cm\u00b2".format(area_1, deci))

#Area of perimeter excluding two semi circles:
ex_2 = area_1 - (2*(area_2))
print("The area of perimeter excluding two semi circles is {0:.{1}f}cm\u00b2".format(ex_2, deci))



