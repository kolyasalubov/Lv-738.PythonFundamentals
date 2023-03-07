def fibo():
    n = int(input('Please enter your desired number of fibonacci numbers: '))
    fibo_list = [0, 1]
    i = 2
    while i<n:
        fibo_list.append(fibo_list[i-2]+fibo_list[i-1])
        i += 1
    print(fibo_list)

fibo()
