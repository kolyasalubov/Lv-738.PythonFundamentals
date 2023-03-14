# Create a simple generator function similar to the range iterator

def my_range(start, finish, step):
    number = start
    while number < finish:
        yield number
        number += step
print(my_range(1, 10, 1))

# for i in my_range(1,10,1):
#     print(i)

f = next(my_range(1, 10, 1))

