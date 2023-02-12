# Write a program that calculates the area of a rectangle S=a*b, the area of a
# triangle S=0.5*h*a, the area of a circle S=pi*r**2. This module must be used in
# another module in which we ask the user the area of which figure he wants to
# calculate.
# (To perform the task, you need to import the "math" module, and from it the
# "pow()" function and the value of the variable "pi", and module, which contains
# three functions for finding areas, into the main program. The basic logic of the
# program is executed in the main module).

import operations

print("""
Area calculator v.2
Press "R" to calculate area of rectangle.
Press "T" to calculate area of triangle.
Press "C" to calculate area of circle.
Or "Q" for quit.
""")

while True:

    user_select = input("Please make your choise R, T, C, or Q : ")

    match user_select:
        case "Q" | "q":
            break
        case "R" | "r":
            side1 = input("Please enter the length of the rectangle : ")
            side2 = input("Please enter the width of the rectangle : ")
            print(f"The area of the rectangle with sides {side1} and {side2} is {operations.rectangle(side1, side2)}\n")
        case "T" | "t":
            base = input("Please enter the size of the base of the triangle : ")
            height = input("Please enter the height of the triangle : ")
            print(f"The area of the triangle with the base {base} and the height {height} is {operations.triangle(base, height)}\n")
        case "C" | "c":
            radius = input("Please enter the radius of the circle : ")
            print(f"\The area of the circle with the radius {radius} is {operations.circle(radius)}\n")
        case _:
            print("Your made the wrong choise, let's try again ...")
            continue
