a, b, c = [int(x) for x in input().split()]
if (a % 2 == 0 and b % 2 == 0 and c % 2 == 0) or (not (a % 2 == 0) and not (b % 2 == 0) and not (c % 2 == 0)):
    print("WIN")
else:
    print("FAIL")
