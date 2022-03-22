n = int(input())
d = {}
for i in range(n):
    a = input()
    if d.get(a):
        d[a] += 1
    else:
        d[a] = 1
arr = list(d.items())
arr.sort(key=lambda x: (-x[1], x[0]))
print(arr[0][0])

