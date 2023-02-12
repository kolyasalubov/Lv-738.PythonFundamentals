print("Task: Regular Ball Super Ball")
# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
# ball1 = Ball()
# ball2 = Ball("super")
# ball1.ball_type  #=> "regular"
# ball2.ball_type  #=> "super"

class Ball(object):
    
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type

ball1 = Ball()
ball2 = Ball("super")
print(ball1.ball_type)  #=> "regular"
print(ball2.ball_type)  #=> "super"
print("")

print("Task: Color Ghost")
# Color Ghost
# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
# ghost = Ghost()
# ghost.color  #=> "white" or "yellow" or "purple" or "red"
import random

class Ghost(object):

    def __init__(self):
        self.color = random.choice("white yellow purple red".split())

ghost = Ghost()
print(ghost.color)  #=> "white" or "yellow" or "purple" or "red"
print("")

print("Task: Basic subclasses - Adam and Eve")
# According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.

# You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and Eve). 
# The first object in the array should be an instance of the class Man. The second should be an instance of the class Woman. 
# Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.
class Human():
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]

print(God())

print("Task: Classy Classes")
# Basic Classes, this kata is mainly aimed at the new JS ES6 Update introducing classes
# Task
# Your task is to complete this Class, the Person class has been created. You must fill in the 
# Constructor method to accept a name as string and an age as number, complete the get Info property 
# and getInfo method/Info getter which should return johns age is 34
# Reference: https://docs.python.org/3/tutorial/classes.html
class Person:

    def __init__(self, name, age):
        self.info=f"{name}s age is {age}"

person = Person("Bob", 21)
print(person.info)
print("")

print("Task: Building Spheres")
# Now that we have a Block let's move on to something slightly more complex a Sphere.
# #Arguments for the constructor:
#     radius -> integer or float (do not round it)
#     mass -> integer or float (do not round it)
# #Methods to be defined
#     get_radius()       =>  radius of the Sphere (do not round it)
#     get_mass()         =>  mass of the Sphere (do not round it)
#     get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
#     get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
#     get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)
# ##Example
#     ball = Sphere(2,50)
#     ball.get_radius() ->       2
#     ball.get_mass() ->         50
#     ball.get_volume() ->       33.51032
#     ball.get_surface_area() -> 50.26548
#     ball.get_density() ->      1.49208
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

print("Task: Building blocks")
# Write a class Block that creates a block (Duh..)
# ##Requirements
# The constructor should take an array as an argument, this will contain 3 integers of 
# the form [width, length, height] from which the Block should be created.
# Define these methods:
#     get_width() return the width of the "Block"
#     get_length() return the length of the "Block"
#     get_height() return the height of the "Block"
#     get_volume() return the volume of the "Block"
#     get_surface_area() return the surface area of the "Block"
# Examples
#     b = Block([2,4,6]) -> create a "Block" object with a width of "2" a length of "4" and a height of "6" 
#     b.get_width() -> return 2
#     b.get_length() -> return 4
#     b.get_height() -> return 6
#     b.get_volume() -> return 48
#     b.get_surface_area() -> return 88
# Note: no error checking is needed
class Block():

    def __init__(self, data):
        self.width = data[0]
        self.length = data[1]
        self.height = data[2]

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.width * self.length * self.height

    def get_surface_area(self): 
        return 2 * (self.width * self.length + self.width * self.height + self.length * self.height)

b = Block([2,4,6]) # create a "Block" object with a width of "2" a length of "4" and a height of "6" 
print(b.get_width()) # return 2
print(b.get_length()) # return 4
print(b.get_height()) # return 6
print(b.get_volume()) # return 48
print(b.get_surface_area()) # return 88
print("")

print("Task: Python's Dynamic Classes #1")
# Timmy's quiet and calm work has been suddenly stopped by his project manager (let's call him boss) yelling:
# - Who named these classes?! Class MyClass? It's ridiculous! I want you to change it to UsefulClass!
# Tim sighed, he already knew it's gonna be a long day.
# Few hours later, boss came again:
# Much better - he said - but now I want to change that class name to SecondUsefulClass,
# and went off. Although Timmy had no idea why changing name is so important for his boss, he realized, 
# that it's not the end, so he turned to you, his guru, to help him and asked you to prepare some function, 
# which could change name of given class.
# Note: Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers), 
# but starting only with upper case letter. In other case it should raise an exception.
# Disclaimer: there are obviously betters way to check class name than in example cases, but let's stick with that, 
# that Timmy yet has to learn them.
#
# Example 1
class MyClass():
    pass

def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise Exception("Wrong name!")
    cls.__name__ = new_name
    print(cls.__name__) # for test

class_name_changer(MyClass, "MyNewClass")

# Example2
import re

class MyClass():
    pass

def class_name_changer(cls, new_name):
    if re.match(r"[A-Z]", new_name[0]) and re.match(r"[A-Za-z0-9]+$", new_name):
        cls.__name__ = new_name
        print(cls.__name__) # for test
    else:
        raise Exception("Wrong name!")
    
class_name_changer(MyClass, "MyNewClass")