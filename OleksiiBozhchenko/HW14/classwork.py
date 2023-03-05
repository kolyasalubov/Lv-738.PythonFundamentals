FILENAME = "somefile.txt"

# my_file = open(FILENAME, "w")        
# my_file.write("Hello SoftServe")
# my_file.close

with open(FILENAME, "w", encoding = "utf-8") as my_file:
    my_file.write("Hello SoftServe")

my_file = open(FILENAME, "a") 
my_file.write("\n")       
my_file.write("Hello Python!!!")
my_file.close

my_file = open(FILENAME, "r")
print(my_file.read())
my_file.close