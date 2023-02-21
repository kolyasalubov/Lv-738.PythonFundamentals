st = "d ioje d yrdsfykkhwuoookjhesgdj atyetqwklslgtalediqrlrurldrtlfsjfey"


def reverse(st):
    new_st = st.split()
    result = []
    fin = ""
    for item in new_st[::-1]:
        result.append(item)
    for it in result:
        fin += (it + " ")

    return fin[:-1]

print(reverse(st))

