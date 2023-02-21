


def rectangle(num1, num2: int):
    return num1 * num2

def triangle(num1, num2, num3: int):
    side_sum = num1 + num2 + num3
    return int(side_sum/2)

def circle(rad: int):
    PI = 3.14
    return PI * rad**2


def choice():
    answer = input("Square of: r/rectangle, t/triangle, c/circle\nNotice: all measurement are in cm.\n ").lower()
    if answer == "r":
        side1 = int(input("First side: "))
        side2 = int(input("Second side: "))
        print(rectangle(side1, side2))
    elif answer == "t":
        side1 = int(input("First side: "))
        side2 = int(input("Second side: "))
        side3 = int(input("Third side: "))
        print(triangle(side1, side2, side3))
    elif answer == "c":
        rad = int(input("Radius: "))
        print(circle(rad))


#-------------------------------------------------


choice()
