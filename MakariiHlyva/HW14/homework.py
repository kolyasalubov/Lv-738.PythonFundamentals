from math import sqrt
from numbers import Number

class Triangle_error(Exception):
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        return repr(self.data)


def square_triangle(a, b, c):
    try:
        if not (isinstance(a, Number)) or not (isinstance(b, Number)) or not (isinstance(c, Number)):
            raise Triangle_error("Triangle sides is not numeric")
        elif a <= 0 or b <= 0 or c <= 0:
            raise Triangle_error("Triangle sides have to be positive number")
        elif (a + b) < c or (a + c) < b or (b + c) < a:
            raise Triangle_error("Triangle with this sides not exist")
        else:
            p = (a + b + c) / 2
            return round(sqrt(p * (p - a) * (p - b) * (p - c)), 5)
    except Triangle_error as error:
        return(error.data)