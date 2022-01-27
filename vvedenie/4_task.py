from typing import List, Tuple


def f_sort(n: int, a: List[int], k: int):
    a.sort()
    left = 0
    right = n - 1
    while a[left] < a[right]:
        if a[left] + a[right] == k:
            print(a[left], " ", a[right])
            return
        elif a[left] + a[right] < k:
            left += 1
        else:
            right -= 1
    print("None")


def f_set(n: int, a: List[int], k: int):
    m = set()
    for i in range(n):
        if k - a[i] in m:
            print(k - a[i], " ", a[i])
            return
        else:
            m.add(a[i])
    print("None")


f_set(int(input()), list(map(int, input().split())), int(input()))
