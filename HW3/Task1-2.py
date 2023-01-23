import os

text = open(os.getcwd() + "/HW3/Zen.txt").read()

print(f"Number of words \"better\" : " + str(text.count("better")))
print(f"Number of words \"never\" : " + str(text.count("never")))
print(f"Number of words \"is\" : " + str(text.count("is")))
print("")

print(text.upper())
print("")

print(text.replace("i", "&"))
print("")

