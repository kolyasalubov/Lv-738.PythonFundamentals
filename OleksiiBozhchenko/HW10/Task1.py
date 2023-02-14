# Task 1.
# Create a polygon class and a rectangle class that inherits from the polygon class and finds the square of rectangle.

class Polygon:
    pass

class Rectangle(Polygon):
    def __init__(self, a, b):
        self.side_a = a
        self.side_b = b

    def rectangle_area(self):
        result = self.side_a * self.side_b
        return print(f"The area of rectangle is {result}")

rectangle_1 = Rectangle(3, 5)
rectangle_1.rectangle_area()


