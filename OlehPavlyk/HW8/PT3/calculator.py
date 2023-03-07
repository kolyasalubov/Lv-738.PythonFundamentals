from math import pi


def rectangle(first_side, second_side):
    return first_side * second_side


def triangle(height, side):
    return 0.5 * height * side


def circle(radius):
    return round(pi * pow(radius, 2), 2)
