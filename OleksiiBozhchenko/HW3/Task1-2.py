import os

text = open(os.getcwd() + "/HW3/Zen.txt").read()

# #
# # Find the number of occurrences of the words "better", "never" and "is" in the given line
# # 
print(f"Number of words \"better\" : " + str(text.count("better")))
print(f"Number of words \"never\" : " + str(text.count("never")))
print(f"Number of words \"is\" : " + str(text.count("is")))
print("")

# #
# # You need to display all text in uppercase (all letters in uppercase)
# #
print(text.upper())
print("")

# #
# # Replace all occurrences of the symbol “i” with “&”
# #
print(text.replace("i", "&"))
print("")

