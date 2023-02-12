countOfCycles = int(input("print the the number of factorial here --> : "))
factorial = 1
answerFactorial = countOfCycles

while countOfCycles > 0:
    factorial = factorial * countOfCycles
    countOfCycles -= 1


print(f"{answerFactorial}! =", factorial)
