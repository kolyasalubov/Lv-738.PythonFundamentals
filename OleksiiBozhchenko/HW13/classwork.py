def bread(func):
    def inner(*args, **kwargs):
        print("<\ ^^^^^^^ />") 
        func(*args, **kwargs) 
        print("<\ ______ />")
    return inner

def greens(func):
    def inner(*args, **kwargs):
        print(" # tomato #") 
        func(*args, **kwargs)
        print(" ~ salad ~") 
    return inner

@bread
@greens
def burger(msg):
    print(msg)

burger("  - meat -")
