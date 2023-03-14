class Car():

    def __init__(self, name, kind, model):
        self.name=name
        self.kind=kind
        self.model=model

    def start(self):
        return print(f"{self.name} started")
    
    def stop(self):
        return print(f"{self.name} stopped")
    

car1 = Car("BMW", "sedan", "X5")
car2 = Car("VW", "truck", "095")

car1.start()
car2.stop()

print(car1.model)
print(car2.model)