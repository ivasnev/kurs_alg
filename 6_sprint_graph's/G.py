from collections import deque


def BFS(s, arr):
    def ShortestPath(v):
        path = deque()
        current_vertex = v
        while current_vertex != None:  # Предшественник вершины s равен None.
            path.append(current_vertex)
            current_vertex = previous[current_vertex]
        return path

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
    print(max(distance))


n, m = map(int, input().split())
arr = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a - 1].append(b - 1)
    arr[b - 1].append(a - 1)
for i in range(n):
    arr[i].sort()
s = int(input())
BFS(s - 1, arr)
