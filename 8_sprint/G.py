n = int(input())
arr = list(map(int, input().split()))
m = int(input())
patter = list(map(int, input().split()))
ind = []
tmp_a = patter[0]
for i in range(len(patter)):
    patter[i] -= tmp_a
for i in range(len(arr)-len(patter)+1):
    tmp_arr = arr[i:i+len(patter)]
    tmp_a = tmp_arr[0]
    for j in range(len(patter)):
        tmp_arr[j] -= tmp_a
    if tmp_arr == patter:
        ind.append(i+1)
print(" ".join(map(str, ind)))

