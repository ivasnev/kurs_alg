def primfacs(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(int(i))
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(int(n))
    return primfac


def task(x, y):
    if x == y:
        return x
    a = primfacs(x)
    a.reverse()
    b = primfacs(y)
    b.reverse()
    if len(a) == 0:
        return b[0]
    if len(b) == 0:
        return a[0]
    obsh = []
    a_unic = []
    b_unic = []
    if len(a) < len(b):
        a, b = b, a
    while len(b) != 0:
        x = b.pop()
        try:
            ind = a.index(x)
            a.pop(ind)
            obsh.append(x)
        except ValueError:
            b_unic.append(x)
    while len(a) != 0:
        a_unic.append(a.pop())
    s = 1
    for i in range(len(obsh)):
        s *= obsh[i]
    b_unic.sort(reverse=True)
    a_unic.sort(reverse=True)
    if len(a_unic) == 0:
        return b_unic[0] * s
    if len(b_unic) == 0:
        return a_unic[0] * s
    return max(a_unic[0], b_unic[0]) * s


for _ in range(int(input())):
    n, m = map(int, input().split())
    print(task(n, m))
