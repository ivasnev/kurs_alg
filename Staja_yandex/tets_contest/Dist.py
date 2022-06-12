def get_s(items, k_f, item_f):
    s = 0
    r = items.index(item_f)
    l = r
    for _ in range(k_f):
        if l - 1 < 0:
            r += 1
            s += abs(item_f - items[r])
        elif r + 1 > len(items) - 1:
            l -= 1
            s += abs(item_f - items[l])
        else:
            if abs(item_f - items[r + 1]) < abs(item_f - items[l - 1]):
                r += 1
                s += abs(item_f - items[r])
            else:
                l -= 1
                s += abs(item_f - items[l])
    return s


n, k = map(int, input().split())
array = list(map(int, input().split()))
array_inp = array.copy()
array.sort()
dict_dist = {}
for i in range(n):
    item = array[i]
    if not dict_dist.get(item):
        dict_dist[item] = 0
for key in dict_dist.keys():
    f = get_s(array, k, key)
    dict_dist[key] = f
print(" ".join([str(dict_dist[x]) for x in array_inp]))
