def f(n, m):
    if n == 0:
        print(0, 1)
        return 0, 1
    else:
        a, b = f(n // 2, m)
        c = a * (2 * b - a) % m
        d = (a ** 2 + b ** 2) % m

        if n % 2 == 0:
            print(c, d)
            return c, d
        else:
            print(d, (c + d) % m)
            return d, (c + d) % m


n, k = map(int, input().split())
print(f(n, 10 ** k)[1])
