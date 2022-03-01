# id 65579141
# Временная сложность O(log(V)(E+V)), где E — количество рёбер в графе, а V — количество вершин
# так как мы используем DFS для поиска цикла
# Сложность по памяти равна O(E) так как мы храним только рёбра
#
from math import log2

def find_cycl_dfs(s):
    flag = False
    color[s] = 1
    for i in arr[s]:
        if color[i] == 0:
            flag = find_cycl_dfs(i)
        elif color[i] == 1:
            return True
    color[s] = 2
    return flag


n = int(input())
color = [0 for i in range(n)]
arr = [[] for x in range(n)]
for y in range(0, n - 1):
    str = input()
    c = len(str) - 1
    for x in range(n - 1, y, -1):
        if str[c] == "R":
            arr[y].append(x)
        else:
            arr[x].append(y)
        c -= 1

flag = False
for i in range(0, n - 1, int(log2(n))+1):
    if find_cycl_dfs(i):
        flag = True
        break

if flag:
    print("NO")
else:
    print("YES")
