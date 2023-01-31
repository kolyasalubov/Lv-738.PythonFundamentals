divisible_by_two = [i for i in range(1,10) if i%2==0]
divisible_by_three = [i for i in range(1,10) if i%3==0 and i%2!=0]
not_divisible = [i for i in range(1,10) if i%2!=0 and i%3!=0]

print("Number divisible by two: ",divisible_by_two)
print("Number divisible by three: ",divisible_by_three)
print("Number not divisible by two and three: ",not_divisible)




a = range(1,10)

for i in a:
    if i%2==0:
        print (i)


for i in a:
    if i%3==0 and i%2!=0:
        print (i)


for i in a:
    if i%2!=0 and i%3!=0:
        print (i)

