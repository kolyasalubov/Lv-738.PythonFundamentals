import random

first = random.randint(0, 10)
second = random.randint(0, 10)
print(f"first number is: {first}, second number is: {second}")
first, second = second, first
print(f"first number is: {first}, second number is: {second}")
