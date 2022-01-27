dict_id = {}
n = int(input())
arr = list(map(int, input().split()))
for i in arr:
    if dict_id.get(i):
        dict_id[i] += 1
    else:
        dict_id[i] = 1
arr = list(dict_id.items())
# for i in list(dict_id):
#     arr.append([dict_id.])
arr.sort(key=lambda x: (x[1], -x[0]), reverse=True)
k = int(input())
for i in range(k):
    print(arr[i][0],end=" ")
