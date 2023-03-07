import random
import math

 
winNumber = random.randint(1, 100)
 
counter = 0

while counter < 10:
    counter += 1
    guess = int(input("Try to guess my number: "))
 
    if winNumber == guess:
        print("Wow, you guessed my number!")
        break
    elif winNumber > guess:
        print("Your number is lower")
    elif winNumber < guess:
        print("Your number is higher")


if counter == 10:
    print("Oops, you used 10 attempts")

   