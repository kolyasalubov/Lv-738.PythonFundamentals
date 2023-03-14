class Human:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello {self.name}!')
    
    @classmethod
    def species (cls):
        print('It is a species Homosapiens')

    @staticmethod
    def method():
        print('Message from static method')

obj1 = Human('Marharyta')
obj1.greeting()
obj1.method()
obj1.species()
obj2 = Human('Illia')
obj2.greeting()
obj2.method()
obj2.species()

