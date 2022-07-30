from collections import deque

s = deque(input())
ans = 0
if len(s) % 2 == 0:
    a = 0
else:
    a = 1
while len(s) != a:
    if s[0] != s[-1]:
        ans += 1
    s.popleft()
    s.pop()
print(ans)

