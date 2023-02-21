import Calculator

mark = input("choose the figure:'rectangle, triangle, circle.'\n-->")
if mark == "rectangle":
    first_param = int(input("write the side a of the rectangle: "))
    second_param = int(input("write the side b of the rectangle: "))
    if first_param > 0 and second_param > 0:
        print(Calculator.area_of_rectangle(first_param, second_param))
    else:
        print("wrong values")
elif mark == "triangle":
    first_param = int(input("write the side  of the triangle: "))
    second_param = int(input("write the height of the triangle: "))
    if first_param > 0 and second_param > 0:
        print(Calculator.area_of_triangle(first_param, second_param))
    else:
        print("wrong values")
elif mark == "circle":
    first_param = int(input("write the radius of the circle: "))
    if first_param > 0:
        print(Calculator.area_of_circle(first_param))
    else:
        print("wrong values")
else:
    print("ERROR: You choose the figure out of list or write incorrect name. Try again")
