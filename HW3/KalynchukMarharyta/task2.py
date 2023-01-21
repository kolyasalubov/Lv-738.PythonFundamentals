number = 7496

#Calculate the product of all digits of the number
product = 1

while number > 0: 
    digit = number%10
    product = product*digit
    number = number//10

print(f'Product is: {product}')

number = 7496

#Convert to string
number_str = str(number)

#Write the number in reverse order by slicing a string
reverse = number_str[::-1]
print(reverse)

#Write numbers in an ascending mode
ascending = sorted(number_str, reverse=True)
print(ascending)