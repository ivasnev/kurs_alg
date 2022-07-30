import sys

sys.setrecursionlimit(100000)


def DFS(v, color, component_count):
    color[v][0] = component_count
    for i in arr[v]:
        if color[i][0] == -1:
            DFS(i, color, component_count)


def find_comp():
    color = [[-1, i] for i in range(n)]
    component_count = 1
    for i in range(n):
        if color[i][0] == -1:
            DFS(i, color, component_count)
            component_count += 1
    color.sort(key=lambda x: (x[0], x[1]))
    print(color[-1][0])
    print(1, end=" ")
    for i in range(1, n):
        if color[i - 1][0] != color[i][0]:
            print()
        print(color[i][1]+1, end=" ")


n, m = map(int, input().split())
arr = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a - 1].append(b - 1)
    arr[b - 1].append(a - 1)
find_comp()
