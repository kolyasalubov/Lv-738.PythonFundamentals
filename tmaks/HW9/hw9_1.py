from random import randint

rand_number = randint(1, 100)
attempts = 0
game_run = True


while game_run:
    user_guess = int(input("What is the number?: "))
    if attempts == 9:
        print("You are out of attempts.")
        game_run = False
    else:
        if user_guess > rand_number:
            print("Your number is bigger, try again.")
            attempts += 1
        elif user_guess < rand_number:
            print("You number is lower, try again.")
            attempts += 1
        elif user_guess == rand_number:
            print("Correct!!!")
            game_run = False






