def my_range(first,second,step=1):
    while first<second:
        yield first
        first += step

for i in my_range(0,10):
    print(i)
