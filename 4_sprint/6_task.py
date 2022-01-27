from collections import Counter
n = int(input())
L = [x for x in input().split()]
Q = []
s = []
for i,x in enumerate(L):
    Q.append(Counter(x))
    if Counter(x) not in s:
        s.append(Counter(x))
differ = len(s)
R = dict()
s = [x.items() for x in s]
for i in range(differ):
    R[frozenset(s[i])] = [i]

Q = [x.items() for x in Q]

for i,x in enumerate(Q):
    R[frozenset(x)].append(i)

Y = list(R.values())

Y.sort(key=lambda x: x[0])


Y = [x[1:] for x in Y]

for x in Y:
    print(' '.join(map(str,x)))