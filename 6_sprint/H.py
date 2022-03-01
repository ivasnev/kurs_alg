import sys
sys.setrecursionlimit(100000)


def DFS(s):
    global time
    entry[s] = time
    color[s] = 1
    time += 1
    for i in arr[s]:
        if color[i] == 0:
            DFS(i)
    leave[s] = time
    time += 1
    color[s] = 2


time = 0
n, m = map(int, input().split())
arr = [[] for i in range(n)]
color = [0 for i in range(n)]
entry = [None for i in range(n)]
leave = [None for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a - 1].append(b - 1)
for i in range(n):
    arr[i].sort()
DFS(0)
for i in range(n):
    print(entry[i],leave[i])
