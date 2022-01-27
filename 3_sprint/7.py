n = int(input())
arr = list(map(int, input().split()))
pink = 0
yellow = 0
malinow = 0
for i in arr:
    if i == 0:
        pink += 1
    elif i == 1:
        yellow += 1
    else:
        malinow += 1
arr = ["0" for i in range(pink)] + ["1" for i in range(yellow)] + ["2" for i in range(malinow)]
print(" ".join(arr))