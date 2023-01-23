number = (input("Enter 4 digits: "))

# find the product of the digits of this number
product = 1
for i in range(len(number)):   
    product *= int(number[i])
print(f"The product of digits of the number is : {product}")

# write the number in reverse order
# reverse_order = list(number[::-1])
# print("(Version1) The reverse order of the number is: " + "".join(reverse_order))

reverse_order = list(number)
reverse_order.reverse()
print("(Version2) The reverse order of the number is: " + "".join(reverse_order))

reverse_order = []
for i in number:   
    reverse_order = [i] + reverse_order
print("(Version3) The reverse order of the number is: "  + "".join(reverse_order))

# in ascending order, you need to sort the numbers included in the given number
print("The sorted digits of the number are: " + "".join(sorted(number)))
