'''2. Assuming that variable forecast has been assigned string 'It will be a sunny day today'
Write Python function corresponding to these assignments:
'''
forecast = "It will be a sunny day today"

#(a) To variable count, the number of occurrences of string 'day' in string forecast.

def a():
    count = forecast.count('day')
    print(count)
a()

#(b) To variable weather, the index where substring 'sunny' starts.

def b():
    weather = forecast.index('sunny')
    print(weather)
b()

#(c) To variable change, a copy of forecast in which every occurrence of substring 'sunny' is replaced by 'cloudy'.

def c():
    change = forecast.replace('sunny','cloudy')
    print(change)
c()


