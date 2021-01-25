

f = open('Txt_RE.txt', 'r')
strs = f.read()
lst = strs.split()
count = 0
for i in lst: 
    

    for j in i:
        if j == 'a' == j == 'e' == j == 'i' == j == 'o' == j == 'u':
            count += 1
print(count)
if len(lst) == len(set(lst)):
    print('Similarity')
else:
    print('It does not hav similarity')





    







































