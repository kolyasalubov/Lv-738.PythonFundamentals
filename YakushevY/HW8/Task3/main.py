from func import rectangle,triang,rounde



figure = input("What shape do you want to calculate the area of?triangle,rectangle,round?: ")

if figure == "triangle" :
    edge = float(input("The size of the side: "))
    heigh = float(input("The size of the heigh: "))
    
    print("Area of ​​your triangle =" , triang(edge,heigh))
elif figure == "rectangle" :
    edge1 = float(input("The size of the first side: "))
    edge2 = float(input("The size of the second side: "))
    print ("Area of ​​your rectangle =",rectangle(edge1,edge2))
elif figure == "round" :
    radius = float(input("The size of the redius: "))
    print("Area of ​​your round =",rounde(radius))
else:
    print("I'm sorry, but we cannot calculate the area of ​​such a figure")
   