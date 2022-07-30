from collections import deque


def BFS(s, arr) -> list:
    color = [0 for i in range(n)]
    previous = [None for i in range(n)]
    distance = [None for i in range(n)]
    planned = deque()
    planned.appendleft(s)
    color[s] = 1
    distance[s] = 0
    while len(planned) != 0:
        u = planned.pop()
        for v in arr[u]:
            if color[v] == 0:
                distance[v] = distance[u] + 1
                previous[v] = u
                color[v] = 1
                planned.appendleft(v)
        color[u] = 2
    return distance


n = int(input())
arr = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    arr[a - 1].append(b - 1)
    arr[b - 1].append(a - 1)
for i in range(n):
    arr[i].sort()

mi = float("inf")
dist = [float("inf") for _ in range(n)]
for i in range(n):
    dist[i] = max(BFS(i, arr))
    mi = min(mi, dist[i])

res = [str(x+1) for x in range(n) if dist[x] == mi]

print(mi, len(res), " ".join(res))
