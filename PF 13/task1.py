
import sqlite3
from sqlite3 import Error


def connect():
    try:
        con = sqlite3.connect('task1.db')
        print('connected')
    except Error:
        print(Error)
    finally:
        print('done')
        return con

'''Programming Exercise 
Task 1 

(a)
'''
'''
def insert_data(con):
    c = con.cursor()
    c.execute("insert into classmates values (10, 'Muqeet', 'gulshan', 20, 'music', 1999)")
    con.commit()
    print('inserted')
    
con = connect()    
insert_data(con)


(b)
'''
'''
def update(con):
    c = con.cursor()
    c.execute("update classmates set friends = 'Fasih' where student_id = 1")
    con.commit()
    print('inserted')

con = connect()
update(con)
'''
'''
(c)
def delete(con):
    c = con.cursor()
    c.execute("delete from classmates where student_id = 9")
    con.commit()
    print('inserted')

(d)
def select(con):
    c = con.cursor()
    c.execute("select * from classmates")
    con.commit()
    print('inserted')

'''


 

#delete(con)



'''Task 2
(a) rows returned: 77
(b) rows returned: 8, Beverages, Condiments, Confections, Dairy Products
Grains/Cereals, Meat/Poultry, Produce, Seafood
(c) records returned: 77
(d) Grains/Cereals// Breads,Creackers,Pasta// Picture
(e) Sets the rows according the the ProductName order of people who have discontinued
(f) gives list of people who havent discontinued
(g) gives unitprice in desencding order
(h) the result will be extracted upon certain conditions such as 
the unit price should be less than 20 and the service should not be discontinued
whereas the data will be ordered in desecnding order of the unit price
(i) #Select AVG(UnitPrice) From Products i.e 28.866
(j) every product that has a unit price greater than the avg and then its 
ordered by the UnitPrice


'''

'''Task 4
'''

import sqlite3
from sqlite3 import Error


def connect():
    try:
        con = sqlite3.connect('links.db')
        print('connected')
    except Error:
        print(Error)
    finally:
        print('done')
        return con
    
con = connect()

'''Practice Problem 12.1
(a)

def a(con):
    c = con.cursor()
    c.execute("select distinct link from hyperlinks where url = 'four.html'")
    con.commit()
    print('task completed')
    
a(con)

'''






















