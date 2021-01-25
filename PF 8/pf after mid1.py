'''
lab  8
'''
#to print the whole dictionary
dict = {'name':'Nasir','fname':'Mahmood'}
print(dict)

#to print the items in the dictionary
for x,y in dict.items():
    print(x, y)

#to print a specific item
print(dict['name'])

#to print the keys in the dictionary
for x in dict.keys():
    print(x)

#to print the values in the dictionary
for x in dict.values():
    print(x)

games = {1:'CSGO',2:'DOTA',3:'WoW'}
print(games)

games[2]='Minecraft'
print(games)

games[4]='Fortnite'
print(games)


#Programming Exercise 1

family = {'My Name':'Muhammad Nasir','Father':'Mahmood Ahmed','Mother':'Uzma Rahat'}

#appending a value with a key other than an integer
family['Paternal GP']='Naseer Ahmed'

family['Maternal GP']='Rauf Tajuddin'
print(family)

#poping
family.pop('Mother')
print(family)

del family['Father']
print(family)



def remove(member):
    
    phone_dir = {}
    
    for i in range(1, 13):
        phone_dir[i] = input("Enter a member: ")
    
    flag = True
    for j in range(1, 13):
        if phone_dir[j] == member:
            phone_dir.pop(j)
            flag = True
            break
        else:
            flag = False
    
    if flag == False:
        return f"{phone_dir}\nMember not in phone directory."
    
    else:
        return f"{phone_dir}"
        
# print(remove('Kashif'))
        
    
#Programming Exercise 2


def delete_num():
    phone = {1:{'Name':'Fasih', 'Type':'Christ-Like', 'Ph':'0301'},
             2:{'Name':'Saif', 'Type':'Patient', 'Ph':'0302'},
             3:{'Name':'Zafir', 'Type':'Nurse', 'Ph':'0303'},
             4:{'Name':'Zen', 'Type':'High','Ph':'0304'},
             5:{'Name':'Mahmood', 'Type':'Father', 'Ph':'0305'}
        
             }
    no = int(input('Enter key: '))
    phone.pop(no)
    count=len(phone)
    print(count)
    print(phone)
delete_num()
print(phone) 


     
#Q3   
def hexAscii(stt):
    i = ord(stt)
    print('{:x}'.format(i))
    
hexAscii('x')


#Q4

dishes = {1:'Chowmein', 2:'Loki Gosht', 3:'Pizza'}
my_list = {1:'Chowmein', 2:'Pizza', 3:'Fish Fillet'}
count = 0
for x in dishes.values():
    for y in my_list.values():
        if x is y:
            count += 1
print(count)

#Q5

def com_guests():
    count = 0
    m_lst = ['Zafir', 'Fasih', 'Ali', 'Saif', 'Zen']
    p_lst = ['Zafir', 'Ali', 'Ahmed', 'Sumail']
    for x in m_lst:
        for y in p_lst:
            if x in y:
                count+=1
    print('There are {} guests in common'.format(count))

def tot_guests():
    m_lst = ['Zafir', 'Fasih', 'Ali', 'Saif', 'Zen']
    p_lst = ['Zafir', 'Ali', 'Ahmed', 'Sumail']
    a = len(m_lst)
    b = len(p_lst)
    c = a + b
    print('Total number of guests are: ', c)
    
com_guests()
tot_guests()












def directory():
    phone = {1:{'Name':'Fasih', 'Type':'Christ-Like', 'Ph':'0301'},
             2:{'Name':'Saif', 'Type':'Patient', 'Ph':'0302'},
             3:{'Name':'Zafir', 'Type':'Nurse', 'Ph':'0303'},
             4:{'Name':'Zen', 'Type':'High','Ph':'0304'},
             5:{'Name':'Mahmood', 'Type':'Father', 'Ph':'0305'}
        
             }
    return phone


    
























    












