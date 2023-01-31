# In the range from 1 to 10 determine
#  - even number that are divisible by 2,
#  - odd numbers which are divisible by 3,
#  - numbers that are not divisible by 2 and 3.

# #
# # Example 1
# #
even = []
odd = []
other = []

for i in range(1, 10):
    if i%2 == 0:
        even.append(i)
    elif i%3 == 0:
        odd.append(i)
    else:
        other.append(i)    

print(f"Even numbers are: {even}\nOdd numbers are: {odd}\nNon divisible numbers are: {other}")

# #
# # Example 2 
# # (In this example I experimented with List Comprehension)
# #
even1  = [i for i in range(1,10) if i%2 == 0]
odd1 = [i for i in range(1,10) if i%3 == 0]
other1 = [i for i in range(1,10) if i%2 != 0 and i%3 != 0]
print(f"Even numbers are: {even1}\nOdd numbers are: {odd1}\nNon divisible numbers are: {other1}")
