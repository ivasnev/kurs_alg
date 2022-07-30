n, m = map(int, input().split())
arr = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a-1].append(b)
for i in range(n):
    arr[i].sort()
    print(len(arr[i]), ' '.join(map(str, arr[i])))
