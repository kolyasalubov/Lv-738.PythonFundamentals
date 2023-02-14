
n = int(input("Enter a number: "))
prev_num = 0
cur_num = 1

for i in range(1, n):
    sum_num = prev_num + cur_num
    prev_num = cur_num
    cur_num = sum_num
    print(cur_num)
