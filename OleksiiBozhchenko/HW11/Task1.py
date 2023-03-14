# Write a program that prompts the user to enter an integer and determines whether
# the number is even or odd, taking into account the case of entering incorrect data.
try: 
  i = int(input("Enter number:"))
  if i % 2 == 0:
    print("even")
  else:
    print("odd")
    
except(ValueError) as e:
  print(f"error: {e}")