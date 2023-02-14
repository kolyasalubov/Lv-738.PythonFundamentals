def nth_smallest(lst, n):
    if n<=len(lst):
        sorted_list = sorted(lst)
        return sorted_list[n-1]
    else:
        return None 