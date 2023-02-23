class Work():

    
    count = 0 

    def __init__(self, first_name,last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        Work.count += 1

    def counter():
        return print(Work.count)

    def warker_info(self):
        print(f"Worker full name: {self.first_name},{self.last_name}\nEmployee salary {self.salary}")

    def class_info():
        print(Work.__base__)
        print(Work.__dict__)
        print(Work.__name__)
        print(Work.__module__)
        print(Work.__doc__)


worke1 = Work("Sania","Klapkovskii", 1140)
worke2 = Work("Lesia","Sokhatska", 1000)
worke3 = Work("Arsen","Kruchko", 1250)
worke4 = Work("luda","Boyko",2300)