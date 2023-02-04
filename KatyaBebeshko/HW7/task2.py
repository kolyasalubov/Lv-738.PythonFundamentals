# Task2. Write a program that calculates the area of a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice).

def rectangleArea(height, width):
    return height*width

def triangleArea(base, height):
    return 0.5*base*height

def circleArea(radius):
    PI=3.14
    return PI*radius**2


while True:
    figure = input("Do you want to calculate area of rectangle, triangle or circle? (Type 'exit' to finish): ")
    match figure:
        case 'rectangle':
            print(rectangleArea(int(input('Please enter height: ')), int(input('Please enter width: '))))
        case 'triangle':
            print(triangleArea(int(input('Please enter base: ')), int(input('Please enter height: '))))
        case 'circle':
            print(circleArea(int(input('Please enter radius: '))))
        case 'exit':
            break
        case _:
            print('Wrong figure. Try Again.')


