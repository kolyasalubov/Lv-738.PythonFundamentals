# # class Polygon:
# #     pass
# #
# #
# # class Rectangle(Polygon):
# #     def __init__(self, a, b):
# #         self.side_a = a
# #         self.side_b = b
# #
# #     def rectangle_area(self):
# #         result = self.side_a * self.side_b
# #         return print(f"Result is {result}")
# #
# #
# # rectangle_1 = Rectangle(8, 5)
# # rectangle_1.rectangle_area()
#
# # def convert(minutes):
# #     if minutes >= 0:
# #         return minutes * 60
# #     else:
# #         pass
#
#
# # def addition(number):
# #     return number + 1
# # def less_than_100(num1, num2):
# #     if num1 + num2 <100:
# #         return True
# #     else:
# #         return False
#
# # def is_isogram(word):
# #
# #     counter = 0
# #     for i in word:
# #         for j in word:
# #             if word[i] == word[j]:
# #                 counter += 1
# #
# #     if counter > 1:
# #         return False
# #     else:
# #         return True
# #
# #
# # print(is_isogram("Algorism"))
#
#
# def filter_list(lst):
#     counter = 0
#     lst1 = []
#
#     for i in lst:
#         try:
#             if isinstance(lst[i], int):
#                 if lst[i] >= 0:
#                     lst1.append(lst[i])
#                 else:
#                     pass
#         except:
#             counter +=1
#
#
#
# lisst = "1fg2hjk3lkj5h4"
# print(filter_list(lisst))
#
#
# # def X_O(word):
# #
# #     counter_o = 0
# #     counter_x = 0
# #     x = len(word)
# #     for i in range(0, x):
# #         if word[i] == "o":
# #             counter_o += 1
# #         elif word[i] == "x":
# #             counter_x += 1
# #
# #     if counter_x == 0 or counter_o == 0 :
# #         return True
# #     if counter_x == counter_o:
# #         return True
# #     else:
# #         return False
# #
# # print(X_O("xoxoxo"))

var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)

import module
module.BOILING_POINT = 100
module.FREEZING_POINT = 0
temperature = float(input())
module.print_water_state(temperature)