#Write a program that prompts the user to enter their age, and then displays a 
# message stating whether the age is even or odd. The program must provide the ability 
# to enter a negative number, and in this case generate an exception. The master code 
# should call a function that processes the information entered


def even_or_odd():
    user_age = int(input('Please enter your age '))
    try:  
        if user_age < 0:
            raise ValueError('Negative value')
        elif user_age % 2 == 0:
            print(f'The age {user_age} is even.')
        else:
            print(f'The age {user_age} is odd.')
    except ValueError as e:
            print(e)
    
even_or_odd()