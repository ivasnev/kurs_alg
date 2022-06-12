n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
for i in range(n):
    arr[i].reverse()
arr.reverse()
for y in range(n-1):
    for x in range(0, m, 2):
        arr[y][x] = arr[y + 1][x]
arr.pop()
print("."*m)
for i in arr:
    print("".join(i))

