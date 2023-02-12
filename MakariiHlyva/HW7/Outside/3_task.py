#--------No yelling!--------#

def filter_words(st):
    str = st.capitalize()
    lst = str.split()
    return ' '.join(lst)

print(filter_words('HELLO CAN YOU HEAR ME'))                   #=> Hello can you hear me
print(filter_words('now THIS is REALLY interesting'))          #=> Now this is really interesting
print(filter_words('THAT was EXTRAORDINARY!'))                 #=> That was extraordinary!