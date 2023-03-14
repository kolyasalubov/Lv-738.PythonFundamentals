import math
import random
import re


class Ball(object):
    
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type

ball1 = Ball()
ball2 = Ball("super")
print(ball1.ball_type)  
print(ball2.ball_type) 


class Ghost(object):
    def __init__(self):
        colors = ["white","yellow","purple","red"]
        self.colors = random.choice(["white","yellow","purple","red"])
    
        print(self.colors)


class Human():
    pass

class Adam(Human):
    pass

class Eva(Human):
    pass

def God():
    return [Adam(), Eva()]

print(God())



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f'{name}s age is {age}'


class Sphere():

    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        print(self.radius)

    def get_mass(self):
        print(self.mass)

    def get_volume(self):
        print(round(4/3 * math.pi * math.pow(self.radius, 3), 5))

    def get_surface_area(self):
        print(round(4 * math.pi * math.pow(self.radius, 2), 5))

    def get_density(self):
        print(round(self.mass / self.get_volume(), 5))

ball = Sphere(2,50)
ball.get_radius()
ball.get_mass()
ball.get_volume()
ball.get_surface_area()
ball.get_density()



class MyClass():
    pass

def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise Exception("Wrong name!")
    cls.__name__ = new_name
    print(cls.__name__) 

class_name_changer(MyClass, "MyNewClass")


class MyClass():
    pass

def class_name_changer(cls, new_name):
    if re.match(r"[A-Z]", new_name[0]) and re.match(r"[A-Za-z0-9]+$", new_name):
        cls.__name__ = new_name
        print(cls.__name__) 
    else:
        raise Exception("Wrong name!")
    
class_name_changer(MyClass, "MyNewClass")