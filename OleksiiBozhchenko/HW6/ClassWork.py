# Create a list of integers that are entered from the terminal and determine the maximum 
# and minimum number among them.
numbers = list(input("Please enter numbers separated by comma : ").split(","))
lst =[]
for i in range(len(numbers)):
    lst.append(int(numbers[i]))
print(f"Min value is: {min(lst)}\nMax value is: {max(lst)}")

# for i in range(0, 100, 2):
#   print(i)

# i=0
# while i < 101:
#   i=i+2
#   print(i)


# for i in range(0, 100):
#   if i%2 == 0:
#     continue
#   else:
#     print(i)

# i=0
# while i < 101:
#   if i%2 == 1:
#     print(i)
#   i += 1 

# for i in [32, 35, 71]:
#   if i%2 == 1:
#     print(i)
#     break
