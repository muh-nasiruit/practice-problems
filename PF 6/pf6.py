''' 6. Implement function cheer() that takes as input a team name (as a string) and prints a cheer as
shown:
>>> cheer('uitians')
How do you spell winner?
I know, I know!
U I T I A N S !
And that's how you spell winner!
Go Uitians!
'''

def cheer(n):
    print('How do you spell winner ?\nI know, I know!')
    t = n.upper()
    print('{} {} {} {} {} {} {} !'.format(t[0], t[1], t[2], t[3], t[4], t[5], t[6]))
    print('And that\'s how you spell winner!\nGo {}!'.format(n.title()))
cheer('uitians')

