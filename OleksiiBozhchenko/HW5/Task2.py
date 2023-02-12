# Print Fibonacci numbers up to the entered number n, using cycles.
# (Sequence of Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, etc.)

# # 
# #  Example 1
# # 
n = int(input("Please enter a number: "))
a = 0
b = 1
row = []
while True:
    if a > n:
        break
    else:
        row.append(a)
        a = a + b
        a, b = b, a
print(row)

# # 
# #  Example 2
# # 
n = int(input("Please enter a number: "))
a = 0
b = 1
row = []
while a <= n:
    row.append(a)
    a = a + b
    a, b = b, a
print(row)
