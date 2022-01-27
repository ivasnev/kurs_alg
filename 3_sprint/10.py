N = int(input())
a = list(map(int, input().split()))
flag_z = True
for i in range(N - 1):
    flag = False
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            flag = True
            flag_z = False
    if flag:
        print(" ".join(map(str, a)))
if flag_z:
    print(" ".join(map(str, a)))