n, m = map(int, input().split())
arr = [[0 for j in range(n)] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a - 1][b-1] = 1
for i in range(n):
    print(' '.join(map(str, arr[i])))
