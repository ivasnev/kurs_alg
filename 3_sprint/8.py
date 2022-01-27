import functools


def comp(a, b):
    a_len = len(a)
    b_len = len(b)
    len_i = a_len if a_len == b_len else a_len + b_len
    for i in range(len_i):
        ac = a[i] if i < a_len else b[i - a_len]
        bc = b[i] if i < b_len else a[i - b_len]
        if ac == bc:
            continue
        return -1 if ac < bc else 1
    return 0


n = int(input())
arr = list(map(str, input().split()))
arr.sort(key=functools.cmp_to_key(comp), reverse=True)
for i in arr:
    print(i, end="")
