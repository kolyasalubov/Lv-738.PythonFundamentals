#--------Reversing Words in a String--------#

def reverse(st):
    lst = st.split()
    lst.reverse()
    return ' '.join(lst)

print(reverse("Hello World"))
print(reverse("Hi There."))