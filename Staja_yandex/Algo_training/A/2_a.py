d = {}
a = int(input())
while a != 0:
    if d.get(a):
        d[a] += 1
    else:
        d[a] = 1
    a = int(input())
print(max(list(d.items()))[1])
