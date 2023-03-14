#----------This program calculate area of different figures--------#


from math import sqrt

# Parent class to init figure 

class Polygon:
    def __init__(self, quantity_of_sides):
        self.quantity = quantity_of_sides
        self.sides = []
        for i in range(0, quantity_of_sides, 1):
            self.sides.append([])

    def inputSides(self):                                                                                         # input sizes of sides
        for i in range(0, self.quantity, 1):
            while True:
                try:
                    l_element = float(input(f"Please, enter length of {i + 1 } side: "))
                    if l_element <= 0:
                        raise ValueError("Length have to be positive and bigger then 0")
                    else:
                        self.sides[i] = l_element
                    break
                except (TypeError, ValueError) as er:
                    print(f"You wrote not correct length! {er}")

    def showSides(self):                                                                                            # show sides of figure 
        for i in range(0, self.quantity, 1):
            print(f"Side {i + 1} - {self.sides[i]}")


class Rectangle(Polygon):                                                                                           
    def __init__(self):                                                                                             # init figure with 2 sides
        super().__init__(2)

    def calculateArea(self):                                                                                        # calculate area of rectangle
        x, y = self.sides
        area = x * y
        print(f"Area of rectangle with sides {x}, {y} is {area}")

class Triangle(Polygon):
    def __init__(self):                                                                                             # inits figure with 3 sides
        super().__init__(3)

    def check_triangle(self):                                                                                       # checks is triangle with this sides exist                                                          
        x, y, z = self.sides
        if (x + y > z) and (x + z > y) and (y + z > x):
            return True
        else:
            return False

    def calculateArea(self):                                                                                        # calculates area of triangle
        x, y, z = self.sides
        p = (x + y + z) / 2
        area = sqrt(p * (p - x) * (p - y) * (p - z))
        print(f"Area of triangle with sides {x}, {y}, {z} is {area}")

class Square(Polygon):
    def __init__(self):                                                                                             # init figure with one side (square)
        super().__init__(1)

    def calculateArea(self):                                                                                        # calcilates area of square 
        x = self.sides[0]
        area = x * x
        print(f"Area of square with sides {x} is {area}")

# Function with helps user to chose figure type and

def input_menu():
    while True:
        try:
            print("Please enter figure type\n 'r' - for rectangle\n't' - for triangle\n's' - for squre")
            figure = input("Please, enter type of figure: ")
            match figure:
                case 'r':
                    rec = Rectangle()
                    rec.inputSides()
                    rec.showSides()
                    rec.calculateArea()
                case 't':
                    tr = Triangle()
                    while True:
                        try:
                            tr.inputSides()
                            if tr.check_triangle():
                                tr.showSides()
                                tr.calculateArea()
                                break
                            else:
                                raise ValueError
                        except ValueError:
                            print("Not correct sizes of triangle, try again")
                    
                case 's':
                    sq = Square()
                    sq.inputSides()
                    sq.showSides()
                    sq.calculateArea()
                case other:
                    raise ValueError
            break
        except ValueError:
            print("Make correct choise from the list above")

input_menu()