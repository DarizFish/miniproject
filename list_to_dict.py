

def list2dict(li, n):
    d = {}
    for index, item in enumerate(li):

        group = index % n
        if group not in d.keys():
            d[group] = [item]
        else:
            d[group].append(item)
    return d


print(list2dict(list(range(10)), 3))