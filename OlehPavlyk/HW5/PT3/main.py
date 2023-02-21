fib = int(input("print the number, you want the Fibonacci numbers go up to "))


def fibonacci(stopper):
    var = [0, 1]
    num = 0
    while num < stopper:
        num = var[-1] + var[-2]

        if num < stopper:
            var.append(num)
    print("Fibonacci numbers: ", var)


fibonacci(fib)
