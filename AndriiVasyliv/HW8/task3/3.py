import operations

print("Which shape's area do you want to calculate?")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")
print("4. Quite")

while True:
    
    choice = int(input("Enter your choice (1-4): "))
    
    match choice:
        case 4:
            break
        case 1:
            a = float(input("Enter the length of the rectangle: "))
            b = float(input("Enter the width of the rectangle: "))
            print("The area of the rectangle is:", operations.rectangle_area(a, b))
        case 2:
            a = float(input("Enter the base of the triangle: "))
            h = float(input("Enter the height of the triangle: "))
            print("The area of the triangle is:", operations.triangle_area(a, h))
        case 3:
            r = float(input("Enter the radius of the circle: "))
            print("The area of the circle is:", operations.circle_area(r))
        case _:
               print("Invalid choice")
               continue
