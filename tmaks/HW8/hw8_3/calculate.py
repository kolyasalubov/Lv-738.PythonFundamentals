from math import pi, pow


def rectangle():
    side_a = int(input("First side: "))
    side_b = int(input("Second side: "))
    S = side_a * side_b
    return f"Area of rectangle is {S}"


def triangle():
    height = int(input("Height of triangle: "))
    side = int(input("Side of triangle: "))
    S = 0.5 * height * side
    return f"Area of triangle is {S}"


def circle():
    radius = int(input("Radius of circle: "))
    S = pi * radius**2
    return f"Area of circle is {S}"


def choice(figure):
    if figure == "r":
        return rectangle()
    elif figure == "t":
        return triangle()
    elif figure == "c":
        return circle()

