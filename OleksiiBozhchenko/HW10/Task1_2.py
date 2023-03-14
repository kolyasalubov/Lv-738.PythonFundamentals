# Task 1.
# Create a polygon class and a rectangle class that inherits from the polygon class 
# and finds the square of rectangle.



class Polygon():

    def __init__(self, no_of_sides):
        self.n = no_of_sides
        # self.sides = [0 for i in range(no_of_sides)]
        #
        # Below I detalizated list comprehension for myself
        #
        # self.sides = []
        # for i in range(self.n):
        #     self.sides.append(0)
        # print(self.sides)


    def inputSides(self):
            self.sides = [float(input(f"Input side {str(i+1)}: ")) for i in range(self.n)]
        #
        # Below I detalizated list comprehension for myself
        #
        # for i in range(self.n):
        #     self.sides = [float(input(f"Input side {str(i+1)}: "))]
        # print(self.sides)

    def dispSides(self):
        for i in range(len(self.sides)):
            print(f"Side {i+1} is {self.sides[i]}")

class Triange(Polygon):
    def __init__(self):
        super().__init__(3)

    def triangle_area(self):
        a,b,c = self.sides
        if a <=0 or b <= 0 or c <=0:
            print("The length of the side cannot be less or equal to zero!")
        elif a + b < c or a + c < b or b + c < a:
            print("The triangle does not exist!")
        else:
            s = (a + b + c) / 2
            result = (s * (s - a) * (s - b) * (s - c)) ** 0.5
            return print(f"The area of triangle is {result}")

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def rectangle_area(self):
        a,b = self.sides
        if a <=0 or b <= 0:
            print("The length of the side cannot be less or equal to zero!")
        else:
            result = a * b
            return print(f"The area of rectangle is {result}")

print("triange1")
triange1 = Triange()
triange1.inputSides()
triange1.dispSides()
triange1.triangle_area()

print("rectangle_1")
rectangle_1 = Rectangle()
rectangle_1.inputSides()
rectangle_1.dispSides()
rectangle_1.rectangle_area()