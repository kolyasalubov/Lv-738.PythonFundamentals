# SUBTASK1

zenOfPython = '''1.Beautiful is better than ugly.
2.Explicit is better than implicit.
3.Simple is better than complex.
4.Complex is better than complicated.
5.Flat is better than nested.
6.Sparse is better than dense.
7.Readability counts.
8.Special cases aren't special enough to break the rules.
9.Although practicality beats purity.
10.Errors should never pass silently.
11.Unless explicitly silenced.
12.In the face of ambiguity, refuse the temptation to guess.
13.There should be one-- and preferably only one --obvious way to do it.
14.Although that way may not be obvious at first unless you're Dutch.
15.Now is better than never.
16.Although never is often better than *right* now.
17.If the implementation is hard to explain, it's a bad idea.
18.If the implementation is easy to explain, it may be a good idea.
19.Namespaces are one honking great idea -- let's do more of those!
20.Beautiful is better than ugly.
21.Explicit is better than implicit.
22.Simple is better than complex.
23.Complex is better than complicated.
24.Flat is better than nested.
25.Sparse is better than dense.
26.Readability counts.
27.Special cases aren't special enough to break the rules.
28.Although practicality beats purity.
29.Errors should never pass silently.
30.Unless explicitly silenced.
31.In the face of ambiguity, refuse the temptation to guess.
32.There should be one-- and preferably only one --obvious way to do it.
33.Although that way may not be obvious at first unless you're Dutch.
34.Now is better than never.
35.Although never is often better than *right* now.
36.If the implementation is hard to explain, it's a bad idea.
37.If the implementation is easy to explain, it may be a good idea.
38.Namespaces are one honking great idea -- let's do more of those!Beautiful is better than ugly.
39.Explicit is better than implicit.
40.Simple is better than complex.
41.Complex is better than complicated.
42.Flat is better than nested.
43.Sparse is better than dense.
44.Readability counts.
45.Special cases aren't special enough to break the rules.
46.Although practicality beats purity.
47.Errors should never pass silently.
48.Unless explicitly silenced.
49.In the face of ambiguity, refuse the temptation to guess.
50.There should be one-- and preferably only one --obvious way to do it.
51.Although that way may not be obvious at first unless you're Dutch.
52.Now is better than never.
53.Although never is often better than *right* now.
54.If the implementation is hard to explain, it's a bad idea.
55.If the implementation is easy to explain, it may be a good idea.
56.Namespaces are one honking great idea -- let's do more of those!'''


betterWordsCount = zenOfPython.count('better')
neverWordsCount = zenOfPython.count('never')
isWordsCount = zenOfPython.count('is')
print(betterWordsCount, neverWordsCount, isWordsCount)

uppercaseZen = zenOfPython.upper()
print(uppercaseZen)

replaceIZen = zenOfPython.replace('i','&')
print(replaceIZen)

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

# SUBTASK3
## Interchange the values of two variables without using the third variable.
x = 10
y = 6
x = x + y
y = x - y
x = x - y

print(x, y)


