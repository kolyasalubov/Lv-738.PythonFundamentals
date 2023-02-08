# # Task 1. 
# # Write a game script that randomly generates a number from a range of 1 to 100 
# # and asks the user to guess that number in 10 tries.
# # The program reads the numbers entered by the user and prompts the user whether the guessed number 
# # is greater or less than the number entered by the user. The game must continue until the user has used 10 attempts 
# # and guessed the number. If the user guessed the number, the program prints a congratulatory message, 
# # and if 10 attempts have been exhausted and the user did not have time to guess the number, 
# # then the corresponding message is displayed. (to perform the task, you need to import the random module,
# # and from it the randint() function)

# import random

# number = random.randint(1, 40)
# counter = 0

# while counter <= 9:
#     counter = counter + 1
#     if counter <= 9:
#         print(f"Attempt number {counter}.")
#     else:
#         print("You have one last attempt!")
#     user_number = int(input("Enter you number: "))
#     if user_number == number:
#         print(f"Congratulations! The number {number} was guessed")
#         break
#     elif 1 <= user_number <= 40 and user_number < number:
#         print("Your number is less than expected")
#     elif 1 <= user_number <= 40 and user_number > number:
#         print("Your number is more than expected")
#     elif not 1 <= user_number <= 40:
#         print("Your number is not in range 1 to 40")

import random

number = random.randint(1, 40)
counter = 0

while counter <= 9:
    counter = counter + 1
    if counter <= 9:
        print(f"Attempt number {counter}.")
    else:
        print("You have one last attempt!")
    user_number = int(input("Enter you number: "))
    if user_number == number:
        print(f"Congratulations! The number {number} was guessed")
        break
    elif user_number in range(1,41) and user_number < number:
        print("Your number is less than expected")
    elif user_number in range(1,41)  and user_number > number:
        print("Your number is more than expected")
    else:
        print("Your number is not in range 1 to 40")