from collections import Counter

n = int(input())
s = input()
print(-1, end=" ")
for i in range(1, n):
    c = Counter(s[i - 1:i + 1])
    for l in range(i - 1, -1, -1):
        if c['0'] > c['1']:
            if s[i] == '0':
                print(l + 1, end=" ")
                break
        elif c['0'] < c['1']:
            if s[i] == '1':
                print(l + 1, end=" ")
                break
        c[s[l-1]] += 1
    else:
        print(-1, end=" ")
