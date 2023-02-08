#----------Program for calculating area of different figures---------#


from choose import *


figure = choose_menu()
match figure:
    case "rectangle_area":
        area = rectangle_area()
        print(f"{figure} area is - {area}")
    case "triangle_area":
        area = triangle_area()
        print(f"{figure} area is - {area}")
    case "circle_area":
        area = circle_area()
        print(f"{figure} area is - {area}")
