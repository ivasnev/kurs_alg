def fibon(n, m):
    if n == 0:
        return 0, 1
    else:
        a, b = fibon(n // 2, m)
        c = a * (2 * b - a) % m
        d = (a ** 2 + b ** 2) % m

        if n % 2 == 0:
            return c, d
        else:
            return d, (c + d) % m


n = int(input())
print(fibon(n, 10 ** 9 + 7)[1])
