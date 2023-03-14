class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"
        
        
person1 = Person('John', 30)
print(person1.info)