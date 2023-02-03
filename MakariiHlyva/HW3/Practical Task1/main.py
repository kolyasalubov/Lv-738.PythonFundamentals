#---------------Work with string of Zen of Python file----------------------------

file = open("python.txt", "r")
data_from_file = file.read()

# Find quantity of different word is file
quantity_of_better = data_from_file.count('better')
quantity_of_never = data_from_file.count('never')
quantity_of_is = data_from_file.count("is")

# Printing results
print(f"Quantity of word 'better' in Zen of Python is - {quantity_of_better}")
print(f"Quantity of word 'never' in Zen of Python is - {quantity_of_never}")
print(f"Quantity of word 'is' in Zen of Python is - {quantity_of_is}")

# Print all text in uppercase
uppercase_text = data_from_file.upper()
print(f"\nPrint all text in uppercase: \n\n{uppercase_text}")

# Replase all symbols "i" with "&"
replaced_text = data_from_file.replace('i', '&')
print(f"\n\nText with replaced symbols i:\n\n{replaced_text}")