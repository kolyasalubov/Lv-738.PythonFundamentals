#Time to practice 1

try:
    a = int(input("Enter your number: "))
    if a < 0:
        raise ValueError("Error your number is odd")
    if a > 0:
        raise ValueError("Error your number is even")

except(ValueError) as e:
    print(f"{e}")
