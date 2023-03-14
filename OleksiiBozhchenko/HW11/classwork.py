# Create a Car class with the attributes
# name, kind, model and methods of start and stop,
# which indicate information that the car started or stoped accordingly.

class Car():
  def __init__(self, name, kind, model):
    self.name = name
    self.kind = kind
    self.model = model

  def start(self):
    print(f"{self.name} started")
  
  def stop(self):
    print(f"{self.name} stopped")

c1 = Car("mazda", "sedan", "model123")
c1.start()

c2 = Car("opel", "pickup", "model342")
c2.stop()

# Write a program that prompts the user to enter an integer and determines whether
# the number is even or odd, taking into account the case of entering incorrect data.
try: 
  i = int(input("Enter number:"))
  if i % 2 == 0:
    print("even")
  else:
    print("odd")
    
except(ValueError) as e:
  print(f"Error: {e}")

# Write a program to calculate the divide of two numbers entered by the user
# sequentially through a comma, to predict the case of division by zero, cases of
# syntactic errors and cases of other exceptional situations. Use the else and finally
# blocks
#
# Example 1 (written in class, wrong solution)
#
try:
    number = input("Enter two numbers separated by a comma").split(",")
    res = 0
    for i in number:
        res = res + int(i)
except(ValueError) as e:
    print(f"Error: {e}")
else:
    print(res)
finally:
    print("Bye-bye")
  