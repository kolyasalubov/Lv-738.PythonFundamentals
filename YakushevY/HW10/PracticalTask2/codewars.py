
# import random


# class Ball(object):
    
#     def __init__(self, ball_type = "regular"):
#         self.ball_type = ball_type

# ball1 = Ball()
# ball2 = Ball("super")
# print(ball1.ball_type)  
# print(ball2.ball_type) 


# class Ghost(object):
#     def __init__(self):
#         colors = ["white","yellow","purple","red"]
#         self.colors = random.choice(["white","yellow","purple","red"])
    
#         print(self.colors)


# class Human():
#     pass

# class Adam(Human):
#     pass

# class Eva(Human):
#     pass

# def God():
#     return [Adam(), Eva()]

# print(God())



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.info = f'{name}s age is {age}'
import math

class Sphere():

    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(4/3 * math.pi * math.pow(self.radius, 3), 5)

    def get_surface_area(self):
        return round(4 * math.pi * math.pow(self.radius, 2), 5)

    def get_density(self):
        return round(self.mass / self.get_volume(), 5)

ball = Sphere(2,50)
print(ball.get_radius()) # 2
print(ball.get_mass()) # 50
print(ball.get_volume()) # 33.51032
print(ball.get_surface_area()) # 50.26548
print(ball.get_density()) # 1.49208
print("")