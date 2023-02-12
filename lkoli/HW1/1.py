# print("hello")

# R1 = "link\name\table"
# print(R1)

# R2 = r"link\name\table"
# print(R2)

# name = "John"
# age = 23
# salary = 999.99

# print("%s is %d years old. Your sallary is %.3f $" % (name, age, salary))

#####################################################

default_order = "Hello {}, {} and {}".format('John', 678,'Sean')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print(positional_order)

# # order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print(keyword_order)

# # a = 'John'
# # b = 'Bill'
# # c = 'Sean'

# # default_order = f'Hello {a}, {b} and {c}'

# # print(default_order)


# # age = int(input("Enter your age: "))

# # if age > 18:
# #     print("Hello")
# # else:
# #     print("False")

# # print(123)



# # if 0 or [] or None or 56:
# #     print("Hello")

# # print(10 and [78, 89] and (90, 8) and 56 and [89, 67] and [89])

# age = int(input("Enter your age: "))

# # if age < 12:  #  to 11
# #     print('kid')
# # else:
# #     print("Hello")  #  >50

# print('kid'  if age < 12 else "Hello")






