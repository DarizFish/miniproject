
def delete_nth(order,max_e):

    num_dict = {}
    del_count = 0
    for index in range(len(order)):
        rel_index = index - del_count
        num = order[rel_index]
        num_dict[num] = num_dict.setdefault(num, 0) + 1
        if num_dict[num] > max_e:
            del_count += 1
            del order[rel_index]
    return order
# assert delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1],3) == [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5]