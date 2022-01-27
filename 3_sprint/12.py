n = int(input())
arr_1 = list(map(int, input().split()))
m = int(input())
midl = int(len(arr_1) / 2)
while (True):
    if sum(arr_1[:midl]) > m*2:
        midl = int(len(midl) / 2)
    else:
        midl = midl + int(len(midl) / 2)
