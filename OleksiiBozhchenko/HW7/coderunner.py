print("")
print("Task 1")
# Given a list of numbers and a value n, write a function that returns the probability of choosing a number greater than or equal to n from the list. The probability should be expressed as a percentage, rounded to one decimal place.

# Notes. Precent probability of event = 100 * (num of favourable outcomes) / (total num of possible outcomes)
def probability(lst, num):
  greater=[]
  for i in range(len(lst)):
    if lst[i] >= num:
      greater.append(lst[i])
  res = round(100 * len(greater) / len(lst), 1)

  return res
# print(probability([22,43,4,6],20))
print(probability([5, 1, 8, 9], 6))



print("")
print("Task 2")

# Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...

def add_indexes(lst):
  res = []
  for index in range(len(lst)):
    res.append(index+lst[index])
  return res

print(add_indexes([12,43,21,23]))

print("")
print("Task 3")
# Create a function that takes a list and finds the list of integers that appear an odd number of times.
def find_odd(lst):
  res = []
  for i in range(len(lst)):
    if lst[i]%1 == 0:
      if lst.count(lst[i])%2 !=0:
        if lst[i] not in res:
          res.append(lst[i])
  return res
# def find_odd(lst):
#   res = []
#   for i in range(len(lst)):
#     if lst[i]%1 == 0 and lst.count(lst[i])%2 !=0 and lst[i] not in res:
#           res.append(lst[i])
#  return res

print(find_odd([12.3,13,23,23,23,12,13,18,17]))


print("")
print("Task 4")
# Given an unsorted list, create a function that returns the n-th smallest integer (the smallest integer is the first smallest, the second smallest integer is the second smallest, etc).

# Notes

# n will always be >= 1.
# Each number in the array will be distinct (there will be a clear ordering).
# Given an out of bounds parameter (e.g. a list is of size k), and you are asked to find the m > k smallest integer, return None.
def nth_smallest(lst, n):
  sorted1 = sorted(lst)
  n = n - 1
  if n < len(sorted1):
    res = sorted1[n]
  else:
    res = None  
  return res
print(nth_smallest([12,6,4,32],2))    

print("")
print("Task 5")
# Create a function that takes a list of non-negative integers and strings and return a new list without the strings.

# Notes

# Zero is a non-negative integer.
# The given list only has integers and strings.
# Numbers in the list should not repeat.
# The original order must be maintained.
def filter_list(lst):
  res = []
  for i in range(len(lst)):
    if not isinstance(lst[i], str):
      res.append(lst[i])
  return res

print(filter_list([3,7,4,"txt",88,0,"string","01","123"]))
