# Print all odd numbers less than 100. 
# (write two versions of the code: one using the continue operator, and the other without this operator).

# #
# # Example 1
# #
for i in range(0, 100):
  if i%2 == 0:
    continue
  else:
    print(i)

# #
# # Example 2
# #
i=0
while i <= 100:
  if i%2:
    print(i)
  i = i+1  