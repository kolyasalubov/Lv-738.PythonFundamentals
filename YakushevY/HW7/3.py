def calculates_number(string):
    d = {}

    for i in string:
        d.update([(i,string.count(i))])  
    print(d)

calculates_number("hello")