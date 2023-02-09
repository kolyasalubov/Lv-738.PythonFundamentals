def add_indexes(lst):
    index_sum_list = []
    for index, element in enumerate(lst):
        index_sum_list.append(index+element)
    return index_sum_list