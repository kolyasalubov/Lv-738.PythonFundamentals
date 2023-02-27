import calculator


def result(resolt):
    match resolt:
        case "1":   # rectangle
            first_side = int(input("write the first side of rectangle\n ==> "))
            second_side = int(input("write the second side of rectangle\n ==> "))
            res = calculator.rectangle(first_side, second_side)
            print(f"result: {res}")
        case "2":  # triangle
            height = int(input("write the height of triangle\n ==> "))
            side = int(input("write the side of triangle\n ==> "))
            res = calculator.triangle(height, side)
            print(f"result: {res}")
        case "3":  # circle
            radius = int(input("write the radius of circle\n ==> "))
            res = calculator.circle(radius)
            print(f"result: {res}")
        case _:
            print("Incorrect value, try again")


figures = {1: "rectangle", 2: "triangle", 3: "circle"}
selector = input(f"select a number of figure whose the area you want to calculate \n {figures}\n ==> ")
result(selector)

