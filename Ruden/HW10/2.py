class Human:
    species = 'Homosapiens'

    def __init__(self, name):
        self.name = name
        
    def welcome(self):
        print(f'Welcome {self.name}!')
    
    @classmethod
    def return_species(cls):
        return  cls.species 
        

    @staticmethod
    def arbitrary_message():
        return 'static method called'

person = Human('Max')
person.welcome()

print(person.return_species()) 
print(Human.return_species())    

print(person.arbitrary_message())
print(Human.arbitrary_message())