w = 0
n = int(input())
s = ""
inp = list(map(int, input().split()))
d = {}
for i in range(26):
    d[2**i] = chr(97 + i)
d[2**26] = " "
for x in inp:
    tmp = abs(x - w)
    s += d[tmp]
    w = x
print(s)
