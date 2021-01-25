''' 5. Write multiple functions for making the mark sheet program as you have done in the previous lab.
'''
def m_sheet():
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
m_sheet()