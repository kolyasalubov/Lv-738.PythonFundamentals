def reverse(st):
    lst = st.split()
    lst.reverse()
    return " ".join(lst)


print(reverse('Hello World'))
