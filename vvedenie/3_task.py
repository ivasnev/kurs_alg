from typing import List, Tuple


def f(a: List[int], k: int, ):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] + a[j] == k:
                print(a[i], " ", a[j])
                return
    print("None")


n = input()
f(list(map(int, input().split())), int(input()))
