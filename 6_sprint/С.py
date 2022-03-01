import sys
sys.setrecursionlimit(100000)


def mainDFS():
    for i in range(n):
        if color[i] == 0:
            DFS(i)


def DFS(s):
    stack = []
    stack.append(s)
    while len(stack) != 0:
        v = stack.pop()
        if color[v] == 0:
            color[v] = 1
            stack.append(v)
            for i in arr[v]:
                if color[i] == 0:
                    stack.append(i)
        elif color[v] == 1:
            color[v] = 2



def rec_DFS(s):
    color[s] = 1
    print(s+1)
    for i in arr[s]:
        if color[i] == 0:
            rec_DFS(i)
    color[s] = 2


n, m = map(int, input().split())
arr = [[] for i in range(n)]
color = [-1 for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    color[a - 1] = 0
    color[b - 1] = 0
    arr[a - 1].append(b - 1)
    arr[b - 1].append(a - 1)
for i in range(n):
    arr[i].sort()
s = int(input())
rec_DFS(s-1)
