# SUBTASK2
## find the product of the digits of this number
n = 6895
n1=int(n/1000)
n2=int(n%1000 / 100)
n3=int(n%100 / 10)
n4=int(n%10 / 1)

print(n1, n2, n3, n4)

product = n1*n2*n3*n4
print(product)

## write the number in reverse order
## just print
print(f'{n4}{n3}{n2}{n1}')

## calculate reversed
reversed=n4*1000 + n3*100 + n2*10 + n1
print(reversed)

## in ascending order, you need to sort the numbers included in the given number
list = [n1, n2, n3, n4]
list.sort()
print(list)



