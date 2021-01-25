'''9. Create a dictionary with name, roll number, semester, semester fees, miscellaneous fees, sports
fees per semester etc and it will write paid amount with total. This is for one student; you need to
generate a proper receipt for at least 3 students but same formatting just like fees vouchers
generated from school. Student copy, University Copy and Bank Copy.
'''

def dictionary():
    n = input("Enter your name: ")
    r = input("Enter your roll number: ")
    s = input("Enter your semester: ")
    sf = input("Enter your semester fees: ") #'2,000'
    mf = input("Enter your misc. fees: ") #'150'
    spf = input("Enter sports fees: ") #'50'
    t = str(int(sf)+int(mf)+int(spf)) #'2,200'
    print("######################## STUDENT COPY ########################")
    d = ['Name', 'Roll Number', 'Semester', 'Semester Fees', 'Misc. Fees', 'Sports Fees', 'Total']
    print('{:18} {:18} {:18} {:18} {:18} {:18} {:18}'.format(d[0], d[1], d[2], d[3], d[4], d[5], d[6]))

    print('{:18} #{:18}{:18} ${:18}${:18}${:18}${:18}'.format(n,r,s,sf,mf,spf,t))
    print("\n######################## UNIVERSITY COPY ########################")
    d = ['Name', 'Roll Number', 'Semester', 'Semester Fees', 'Misc. Fees', 'Sports Fees', 'Total']
    print('{:18} {:18} {:18} {:18} {:18} {:18} {:18}'.format(d[0], d[1], d[2], d[3], d[4], d[5], d[6]))
    print('{:18} #{:18}{:18} ${:18}${:18}${:18}${:18}'.format(n,r,s,sf,mf,spf,t))
    print("\n######################## BANK COPY ########################")
    d = ['Name', 'Roll Number', 'Semester', 'Semester Fees', 'Misc. Fees', 'Sports Fees', 'Total']
    print('{:18} {:18} {:18} {:18} {:18} {:18} {:18}'.format(d[0], d[1], d[2], d[3], d[4], d[5], d[6]))
    print('{:18} #{:18}{:18} ${:18}${:18}${:18}${:18}'.format(n,r,s,sf,mf,spf,t))

dictionary()