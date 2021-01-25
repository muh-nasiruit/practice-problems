''' 3. Write a function that can calculate the arithmetic sequence of n numbers. The program will
generate the nth term of the sequence, whereas the user will enter the first term and the common
difference. The program will then ask either to continue or not, if the user will enter yes it will ask
the next nth term to calculate. Example: you have entered the first term as 3 and common
difference 6 you are interesting in 35th term. So it will calculate and generate the answer as 207.
Now it will again ask for you to continue if you agree it will ask next term like 45th or 96th term to calculate.
'''
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
n_th()