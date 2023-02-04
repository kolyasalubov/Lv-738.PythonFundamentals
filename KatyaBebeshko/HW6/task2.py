# Task2. Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is different, send an error message.
# (need to use loop while)

# with count

count=0

while count < 5:
    login = input('Enter login: ')
    if login=='First':
        print('Successful login')
        break
    else:
        print('Access denied. Try again.')
        count += 1

# without count

while input('Enter login: ') != 'First':
    print('Access denied. Try again.')
else:
    print('Successful login')

      