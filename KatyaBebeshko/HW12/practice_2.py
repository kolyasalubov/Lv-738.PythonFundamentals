# Using several decorators, create a sandwich consisting of lettuce, tomatoes and meat. 
# <\ ^^^^^^^ /> 
# # tomato # 
# – meat– 
# ~ salad ~
#  <\ ______ />


def bread(func):
    def wrapper(*args, **kwargs):
        print("<\ ^^^^^^^ />")
        func(*args, **kwargs)
        print("<\ ______ />")
    return wrapper

def vegetables(func):
    def wrapper(*args, **kwargs):
        print("~ salad ~")
        func(*args, **kwargs)
        print("# tomato #")
    return wrapper



@bread
@vegetables
def sandwich():
    print('-meat-')

sandwich()






