# Write a function that returns the arithmetic mean of any number of numbers

# #
# # Example 1
# #
def average (*args):
  res = sum(args)/len(args)
  return(res) 

print(average(7,3,5))


# #
# # Example 2 (without using the sum() and len() functions)
# #
def average2 (*args):
  count = 0
  sum = 0
  i=0
  while i in range(len(args)):
    sum = sum + args[i]
    i += 1
    count += 1
    res = sum / count
  return(res)  

print(average2(4,6,8,2)) 
