n, a, b = map(int, input().split())
if b < a:
    a, b = b, a
print(min(b - a - 1, a + n - b - 1))
