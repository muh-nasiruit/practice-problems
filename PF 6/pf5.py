'''5. Write a function month() that takes a number between 1 and 12 as input and returns the
three-character abbreviation of the corresponding month. Do this without using an if
statement, just string operations. Hint: Use a string to store the abbreviations in order.
>>> month(1)
'Jan'
>>> month(11)
'Nov'
'''

def month(m):
    m_n = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'
    n = str.split(m_n)
    return n[m - 1]
month(3)

























