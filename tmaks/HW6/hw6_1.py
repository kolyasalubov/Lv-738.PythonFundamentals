
even_list = []
odd_list = []
n_div = []

for i in range(1, 11):
    if i % 2 == 1:
        if i % 3 == 0:
            odd_list.append(i)
        elif i % 3 >= 1:
            n_div.append(i)
    else:
        even_list.append(i)
print(f"even divisible by 2 : {even_list}\nodd devisible by 3: {odd_list}\n"
      f"numbers not divisible by 2 nor 3: {n_div}")