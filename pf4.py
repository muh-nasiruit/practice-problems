''' 4. Write a function which will check either the giving string is Palindrome or not. Palindrome is a
string when we reverse the string it will generate the original string. Example CIVIC, MOM, 010,
1001, etc. So if you enter the word which is Palindrome it will say yes your string is Palindrome
otherwise it will generate sorry message.
'''

pal = str(input("Enter a Palindrome: "))
spal = pal.casefold()
def reverse(spal):
    return spal[::-1]
lap = reverse(spal)
if spal == lap: 
    print("Yes")
else:
    print("No")
reverse(spal)

