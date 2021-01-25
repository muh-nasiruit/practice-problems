
# #Programming Exercise

# ##(1)Write a program which solves the quadratic equation. The user will enter the value of a, b and c. The program will then check the denominator that if denominator is zero or not. If its zero it can reply the equation cannot solve as there is a zero division else, it will execute the program and will generate two solutions.

# In[12]:


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
from math import sqrt

d = sqrt(b**2 -4*a*c)

if d == 0: 
    print("No Solution")
else:
    x_1 = (-b+ sqrt(b**2-4*a*c))/(2*a)
    x_2 = (-b -sqrt(b**2-4*a*c))/(2*a)
    print(x_1, x_2)


# ##(2) Calculate the arithmetic sequence of n numbers. The program will generate the nth term of the sequence, whereas the user will enter the first term and the common difference. The program will then ask either to continue or not, if the user will enter yes it will ask the next nth term to calculate. Example: you have entered the first term as 3 and common difference 6 you are interesting in 35 th term. So it will calculate and generate the answer as 207. Now it will again ask for you to continue if you agree it will ask next term like 45th or 96th term to calculate.

# In[32]:


def n_th():
    a = int(input("Enter the first term: "))
    d = int(input("Enter the common difference: "))
    n = int(input("Enter the nth term to be find: "))
    tn = a + (n-1)*d
    print(tn)
n_th()
ask = str(input("Proceed to next term.. ? "))
if ask == 'yes':
    n_th()
else:
    print("solved")


# ##(3) Write a program which will check either the giving string is Palindrome or not. Palindrome is a string when we reverse the string it will generate the original string. Example CIVIC, MOM, 010, 1001, etc. So if you enter the word which is Palindrome it will say yes your string is Palindrome otherwise it will generate sorry message.

# In[15]:


pal = str(input("Enter a Palindrome: "))
def reverse(pal):
    return pal[::-1]
lap = reverse(pal)
if pal == lap: 
    print("Yes")
else:
    print("No")


# ##(4)Write a program which will collect your name, your father’s name, your roll number and your subjects (5 Subjects with name and numbers). At the end it will generate a result with your name, your father’s name, your details subjects, marks you have obtained with total marks with grade and percentage.

# In[2]:


Name = input("Enter Name: ")
FatherName = input("Enter Father Name: ")
RollNumber = int(input("Enter Roll Number: "))
Subjects = []
Marks = []

for i in range(5):
    Subject = input("Enter Subject: ")
    Subjects.append(Subject)
    Mark = int(input("Enter Marks: "))
    Marks.append(Mark)

TotalPercentage = (sum(Marks)/500) * 100

print('Name: {}'.format(Name))
print('Father Name: {} '.format(FatherName))
print('Roll Number: {}'.format(RollNumber))
for i in range(3):
    print('Scored {} in {} out of 100'.format(Marks[i],Subjects[i]))    
print('Total Marks Obtained out of 500 are: {}'.format(sum(Marks)))
print('Percentage Obtained: {}'.format(TotalPercentage))


# ##(5)Generate a table from initial value to final, depending upon the user starting and ending range in matrix form such as:

# In[2]:


i_val = int(input("Enter the intial value: "))
f_val = int(input("Enter the final value: "))
for i in range(i_val, f_val):
    print('{} {:2} {:2} {:2} {:2} '.format(i, 2*i, 3*i, 4*i, 5*i))

