# Write a program that calculate the area of a rectangle, triangle and circle.
# Write three function to calculate the area. And call them in the main program
# depending on the user's choise.

def area_rectangle(side1, side2):
    area = int(side1) * int(side2)
    print(f"\nThe area of the rectangle with sides {side1} and {side2} is {area}\n")

def area_triangle(base, height):
    area = 1/2 * int(base) * int(height)
    print(f"\nThe area of the triangle with the base {base} and the height {height} is {area}\n")

def area_circle(radius):
    area = 3.14 * int(radius)**2
    print(f"\nThe area of the circle with the radius {radius} is {area}\n")

print("""
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
            area_rectangle(side1, side2)
        case "T" | "t":
            base = input("Please enter the size of the base of the triangle : ")
            height = input("Please enter the height of the triangle : ")
            area_triangle(base, height)
        case "C" | "c":
            radius = input("Please enter the radius of the circle : ")
            area_circle(radius)
        case _:
            print("Your made the wrong choise, let's try again ...")
            continue
