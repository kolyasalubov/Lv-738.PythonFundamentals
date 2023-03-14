from random import randint

random_number = randint(1, 100)

attempts = 0
flag = False
guess = int(input(f'Guess the number between 1 and 100, you have 10 attempts. It is attempt number {attempts}. Your number: '))


while attempts < 11:
    if guess < random_number:
        guess = int(input('Please choose a bigger number '))
        attempts += 1
    elif guess > random_number:
        guess = int(input('Please choose a smaller number '))
        attempts +=1
    else: 
        guess == random_number
        flag = True
        print('Congratulations! You have guessed!')
        break 

if flag == False:
    print('Unfortunately, you have taken 10 guesses.')


