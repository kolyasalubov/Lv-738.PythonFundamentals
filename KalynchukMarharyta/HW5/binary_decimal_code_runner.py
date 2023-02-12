def binary(decimal):
    lst = []
    number = int(decimal)
    if number == 0:
        return 0
    while number > 0:
        i = number%2 
        lst.append(i)
        number = number//2
    bin_num = ''.join([str(item) for item in lst])
    return bin_num[::-1]
    
