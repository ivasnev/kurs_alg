n = int(input())
m = int(input())
array = [[] for j in range(m)]
for i in range(n):
    tmp_arr = [int(x) for x in input().split()]
    for j in range(m):
        array[j].append(tmp_arr[j])

for i in range(m):
    print(' '.join(map(str, array[i])))






