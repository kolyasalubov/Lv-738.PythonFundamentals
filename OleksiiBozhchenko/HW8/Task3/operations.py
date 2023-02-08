import math

def rectangle(side1, side2):
    area = int(side1) * int(side2)
    return area

def triangle(base, height):
    area = 1/2 * int(base) * int(height)
    return area

def circle(radius):
    area = math.pi * math.pow(int(radius),2)
    return area