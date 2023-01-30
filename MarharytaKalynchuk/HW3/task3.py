a = 9000000
b = 1111111

b=str(b)+'*'+str(a)
a=int(b.split('*')[0])
b=int(b.split('*')[1])

print(a,b)