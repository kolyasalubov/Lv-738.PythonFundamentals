#--------Program calculate areas of different objects-------#


from math import pi


# Function for getting data from console

def enter_data(object_type):
    """This Function takes data from console"""

    if object_type == "Circle":
        while True:
            try:
                radius = float(input(f"\nPlease enter radious of {object_type}: "))
                break
            except ValueError:
                print("'\nArgument, you are enterng should be a number, try again")
            else:
                break
        print("\n", area_circle.__doc__)
        area_circle(radius)
    else: 
        while True:
            try:
                height = float(input(f"\nPlease enter heigh of {object_type}: "))
                break
            except ValueError:
                print("\nArgument, you are enterng should be a number, try again")
            else:
                break
        while True:
            try:
                width = float(input(f"\nPlease enter width of {object_type}: "))
                break
            except ValueError:
                print("\nArgument, you are enterng should be a number, try again")
            else:
                break
    if object_type == "Triangle":
        print("\n", area_triangle.__doc__)
        area_triangle(height, width)
    if object_type == "Rectangle":
        print("\n", area_rectangle.__doc__)
        area_rectangle(height, width)


# Function for calculating area of rectangle

def area_rectangle(height, width):
    """This Functuion calculate area of rectangle"""

    print(f"Area of rectagle with sizes {height} X {width} - ", height * width)


# Function for calculating area of triangle

def area_triangle(height, width):
    """This function calculate area of triangle"""

    print(f"Area of triangle with h = {height} and width = {width} - ", height * width / 2)


# Function for calculating area of circle

def area_circle(radius):
    """This function calculate area of circle"""

    print(f"Area of circle whith r = {radius} - ", round((pi * radius**2), 2))


# This function shows main menu in console

def main_menu():
    """This functiuon shows main menu"""


    while True:
        try:
            print("Chose type of odject:\n'T' or 't' for Triangle\n'R' or 'r' for Rectangle\n'C' or 'c' for Circle")
            symbol = str(input("Please enter type of object: "))
            if symbol == "T" or symbol == 't':
                object_type = "Triangle"
            elif symbol == "R" or symbol == "r":
                object_type = "Rectangle"
            elif symbol == "C" or symbol == "c":
                object_type = "Circle"
            else:
                raise ValueError
        except ValueError:
            print("\nArgument, you are enterng should be from the list")
        else:
            break
    return object_type

print(main_menu.__doc__)
enter_data(main_menu())
