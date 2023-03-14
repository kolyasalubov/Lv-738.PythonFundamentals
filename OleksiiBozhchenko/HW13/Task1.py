# Create a simple generator function similar to the range iterator

def range_iterator(start, finish, step):
    while start < finish:
        yield start
        start = start + step

for i in range_iterator(2,14,3):
    print(i)