'''10. Compare two brands of petrol prices in Pakistan:
PSO and Shell
Pakistan Oil Prices, Pakistan Petroleum Prices and current Petrol Prices
PSO
Type Price
Premium (Super) Rs. 114.24 /Ltr
High Speed Diesel Rs. 127.41 /Ltr
Light Speed Diesel Rs. 85.33 /Ltr
Kerosene Oil Rs. 97.18 /Ltr
Shell
Product Name Rs./litre
E10 Gasoline 111.74
Altron Premium 114.24
Action + Diesel 127.41
LDO 85.33
SKO 97.18
Find that if a user can extract the amount of Petrol for a month where monthly petrol is 500 liters, 300
liters’ diesel and 200 liters of kerosene oil. What is the difference between the amount in both? Keep in
mind proper formatting is required.
'''

print('PSO\t\tShell\t\tFor 500 ltrs/month\tFor 300 ltrs/month\tFor 200 ltrs/month')
d = []
d.append([114.24, 111.74])
d.append([127.41, 114.24])
d.append([85.33,127.41])
d.append([97.18,85.33])    

def compare(d):
    for i in d:
        print('''Rs{:7}\tRs{:7}\tRs{:8.8}\t\tRs{:8.8}\t\tRs{:8.8}'''.format(i[0], i[1], abs(500*i[1]-i[0]*500), abs(300*i[1]-i[0]*300), abs(200*i[1]-i[0]*200)))
compare(d)
