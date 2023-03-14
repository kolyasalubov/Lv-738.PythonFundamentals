class Polygon:
    def __init__(self,side):
        self.sid = side
        self.sides =[]

    def what_side(self):
        for i in range(self.sid):
            
            ad = float(input(f"Enter side {i+1} :"))
            self.sides.append(ad)
            
        print(self.sides)

    
class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)
    def area_find(self):
        b,c,d = self.sides
        p = (b+c+d)/2
        area = (p*(p-b)*(p-c)*(p-d))**0.5
        if d <b +c:
            print ("You will not get a triangle from your sides")
        elif b <d +c:
            print ("You will not get a triangle from your sides")
        elif c <b +d:
            print ("You will not get a triangle from your sides")
        else:
            print(area)
a = Triangle()
a.what_side()
a.area_find()
