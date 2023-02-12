import task3_area_functions as areas

while True:
    figure = (input("Select number of the figure you want calculate area of 1 - rectangle 2 - triangle 3 - circle? (Type 'q' to finish): "))
    match figure:
        case "1":
            print(areas.rectangleArea(int(input('Please enter height: ')), int(input('Please enter width: '))))
        case "2":
            print(areas.triangleArea(int(input('Please enter base: ')), int(input('Please enter height: '))))
        case "3":
            print(areas.circleArea(int(input('Please enter radius: '))))
        case 'q':
            break
        case _:
            print('Wrong figure. Try Again.')