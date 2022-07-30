from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


d = int(input())
x, y = map(int, input().split())
if 0 <= x <= d and 0 <= y <= d and y <= -x + d:
    print(0)
else:
    a = distance(x, y, 0, 0)
    b = distance(x, y, d, 0)
    c = distance(x, y, 0, d)
    if a == min(a, b, c):
        print(1)
    elif b == min(a, b, c):
        print(2)
    else:
        print(3)
