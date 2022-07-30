def check_full():
    for x in range(n):
        if len(arr[x]) != n - 1:
            return "NO"
    return "YES"


n, m = map(int, input().split())
arr = [set() for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    if a != b:
        arr[a - 1].add(b - 1)
        arr[b - 1].add(a - 1)

print(check_full())