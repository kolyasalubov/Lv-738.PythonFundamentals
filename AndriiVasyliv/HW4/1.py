########This is practical task

# a = int(input("Enter first numbers "))
# b = int(input("Enter second numbers "))

# if a > b:
#     print(f"Your number {a} is more than {b}")
# elif a < b:
#     print(f"Your number {a} is less than {b}")
# elif a == b:
#     print(f"Your numbers equal {a} = {b}")

###################################################    
    
# num = int(input("Enter a number: "))
# mod = num % 2
# if mod > 0:
#     print(f"{num} is an odd number.")
# else:
#     print(f"{num} is an even number.")

####################################################

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)