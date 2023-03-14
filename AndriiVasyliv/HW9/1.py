import random

number_to_guess = random.randint(1, 50)
attempts_left = 10

print("Guess the number from 1 to 50. You have 10 attempts.")

while attempts_left > 0:
    guess = input(f"Attempt {11 - attempts_left}. Your guess: ")
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a number")
        continue

    if guess == number_to_guess:
        print(f"Congratulations, your number {guess} is guessed!")
        break
    elif guess < number_to_guess:
        print("The number is less")
    else:
        print("The number is more")

    attempts_left -= 1

if attempts_left == 0:
    print(f"You lost! The number was {number_to_guess}.")
