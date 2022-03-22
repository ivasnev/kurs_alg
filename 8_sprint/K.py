a = "".join([x for x in input() if ord(x) % 2 == 0])
b = "".join([x for x in input() if ord(x) % 2 == 0])
if a < b:
    print(-1)
elif a > b:
    print(1)
else:
    print(0)
