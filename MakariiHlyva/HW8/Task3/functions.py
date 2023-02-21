#---------list of functions for calculating area of different functtions---------#


from math import pi

# Function for calculating rectangle area and return it

def rectangle_area():

    """This function will calculate rectangle area"""
    
    while True:
        try:
            a = float(input("Please, enter size a = "))
            b = float(input("Please, enter size b = "))
            if (type(a), type(b) == float) and (a > 0 and b > 0):
                s = a * b
                return s
            else:
                raise ValueError
        except ValueError:
            print("Sizes have to be natural and float, try again")


# Function for calculating triangle area and return it

def triangle_area():

    """This function will calculate triangle area"""

    while True:
        try:
            a = float(input("Please, enter size of triangle base a = "))
            h = float(input("Please, enter height h = "))
            if (type(a), type(h) == float) and (a > 0 and h > 0):
                s = 0.5 * a * h
                return s
            else:
                ValueError
        except ValueError:
            print("Sizes have to be natural and float, try again")
        else:
            break
        
    

# Function for calculating circle area and return it

def circle_area():

    """This function will calculate circle area"""

    while True:
        try:
            r = float(input("Please, enter radius r = "))
            if type(r) == float and r > 0:
                s = pi * r * 2
                return s
            else:
                raise ValueError
        except ValueError:
            print("Radius have to be natural and float, try again")
