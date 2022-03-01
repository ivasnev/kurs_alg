import sys

sys.setrecursionlimit(100000)


def topologicalSortUtil(v, visited, stack):
    visited[v] = True
    for i in arr[v]:
        if visited[i] == False:
            topologicalSortUtil(i, visited, stack)
    stack.append(v + 1)


def topologicalSort():
    visited = [False] * n
    stack = []
    for i in range(n):
        if visited[i] == False:
            topologicalSortUtil(i, visited, stack)
    for i in range(n - 1, -1, -1):
        print(stack[i], end=" ")


n, m = map(int, input().split())
arr = [[] for i in range(n)]
color = [0 for i in range(n)]
order = []

for i in range(m):
    a, b = map(int, input().split())
    arr[a - 1].append(b - 1)
topologicalSort()