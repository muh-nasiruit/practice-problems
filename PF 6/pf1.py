#Programming Exercises PF Lab 06

'''1. Construct the strings by using the string time format function strftime ()
'''

#(a) (‘Monday, November 25 2019')

import time
time.strftime('%A, %B %d %Y', time.localtime())

#(b) ('09:40 PM Central Daylight Time on 11/25/2019')

time.strftime('%I:%M %p Central Daylight Time on %b/%d/%y', time.localtime())

#(c) ('I will meet you on Thu July 13 at 09:40 PM.')

time.strftime('I will meet you on %a %B at %I:%M %p.', time.localtime())
