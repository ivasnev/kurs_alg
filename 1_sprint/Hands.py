#id 58813213

import collections

k = int(input())
d = collections.defaultdict(int)
for i in range(4):
    inp = list(input())
    for j in range(4):
        if inp[j] != '.':
            d[int(inp[j])] += 1
res = 0
for i in d:
    if d[i] <= 2*k:
        res += 1
print(res)
