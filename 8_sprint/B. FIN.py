# id 66444836
# Временная сложность BFS O(V + E), где E — количество рёбер в графе, а V — количество вершин
# Временная сложность создания и инициализации бора тоже O(V + E) ведь мы используем обход в ширину
# Временная сложность функции водителя O(N), где N длина строки
# Сложность по памяти O(N*M), где N длина строки а M максимальное колличество вхождений подстроки в строку

from collections import deque


def BFS(s, arr):
    white = 0
    grey = 1
    black = 2
    color = [white for _ in range(len(arr))]
    planned = deque()
    planned.appendleft(s)
    color[s] = grey
    while len(planned) != 0:
        u = planned.pop()
        for v in arr[u]:
            if color[v] == white:
                color[v] = grey
                planned.appendleft(v)
        color[u] = black
    return color


class AhoNode:
    def __init__(self):
        self.goto = {}
        self.out = []
        self.fail = None


def aho_create_forest(patterns):
    root = AhoNode()
    for path in patterns:
        node = root
        for symbol in path:
            node = node.goto.setdefault(symbol, AhoNode())
        node.out.append(path)
    return root


def aho_create_statemachine(patterns):
    root_tmp = aho_create_forest(patterns)
    queue = []
    for node in root_tmp.goto.values():
        queue.append(node)
        node.fail = root_tmp
    while len(queue) > 0:
        rnode = queue.pop(0)
        for key, unode in rnode.goto.items():
            queue.append(unode)
            fnode = rnode.fail
            while fnode is not None and key not in fnode.goto:
                fnode = fnode.fail
            unode.fail = fnode.goto[key] if fnode else root_tmp
            unode.out += unode.fail.out
    return root_tmp


def aho_find_all(s, root_a):
    node = root_a
    res = {}
    for i in range(len(s)):
        while node is not None and s[i] not in node.goto:
            node = node.fail
        if node is None:
            node = root_a
            continue
        node = node.goto[s[i]]
        for pattern in node.out:
            if res.get(i - len(pattern) + 1):
                res[i - len(pattern) + 1].append(i + 1)
            else:
                res[i - len(pattern) + 1] = [i + 1]
    if len(res) == 0:
        return -1
    else:
        return res


def main():
    shpora = input()
    n = int(input())
    keys = set()
    for _ in range(n):
        keys.add(input())
    root = aho_create_statemachine(keys)
    d = aho_find_all(shpora, root)
    nodes = [[] for _ in range(len(shpora) + 1)]
    for i in range(len(nodes)):
        tmp = d.get(i)
        if type(tmp) is list:
            nodes[i] = tmp
    if BFS(0, nodes)[-1] == 2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
