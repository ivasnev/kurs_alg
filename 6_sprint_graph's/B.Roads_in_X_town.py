# id 65682114
# Временная сложность O(E+V), где E — количество рёбер в графе, а V — количество вершин
# так как мы используем DFS для поиска цикла
# Сложность по памяти равна O(E) так как мы храним только рёбра
#

def find_cycl_dfs(s, color_f, arr_f):
    flag_f = False
    color_f[s] = 1
    for i in arr_f[s]:
        if color_f[i] == 0:
            flag_f = find_cycl_dfs(i, color_f, arr_f)
        elif color_f[i] == 1:
            return True
    color_f[s] = 2
    return flag_f


def input_gr():
    n_f = int(input())
    color_f = [0 for _ in range(n_f)]
    arr_f = [[] for _ in range(n_f)]
    for y in range(0, n_f - 1):
        str_f = input()
        c = len(str_f) - 1
        for x in range(n_f - 1, y, -1):
            if str_f[c] == "R":
                arr_f[y].append(x)
            else:
                arr_f[x].append(y)
            c -= 1
    return n_f, color_f, arr_f


def main():
    n, color, arr = input_gr()
    flag = False
    for i in range(n):
        if color[i] == 0:
            if find_cycl_dfs(i, color, arr):
                flag = True
                break
    if flag:
        print("NO")
    else:
        print("YES")


main()
