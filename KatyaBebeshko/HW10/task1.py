# Task1. Create a polygon class and a rectangle class
# that inherits from the polygon class and finds the square
# of rectangle.

class Polygon:
    pass

class Rectangle(Polygon):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def rectangleArea(self):
        return self.height * self.width

rectangleTest = Rectangle(2, 10)
print(rectangleTest.rectangleArea())