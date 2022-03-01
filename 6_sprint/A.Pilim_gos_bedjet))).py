# ID 65578535
# Временная сложность O(E⋅logV), где E — количество рёбер в графе, а V — количество вершин
# Скорость поиска max O(1) благодаря приор. очереди. шагов требуется по кол рёбер
# Сложность по памяти мы имеем 2 сета в сумме дающие V элементов, матрицу связи с весами размера V^2,
# и приор. очеред. или древо хранящая рёбра в худшем случае V-1 ребро следовательно сложность по памяти,
# будет O(V^2)
#

from queue import PriorityQueue


def input_data():
    n, m = map(int, input().split())
    weight = [[None for y in range(n)] for x in range(n)]
    for i in range(m):
        a, b, c = map(int, input().split())
        if weight[a - 1][b - 1] is None or -1 * weight[a - 1][b - 1] < c:
            weight[a - 1][b - 1] = -c
            weight[b - 1][a - 1] = -c
    return n, m, weight


def add_vertex(start, edges, weight):
    added.add(start)
    not_added.remove(start)
    for e in [[weight[start][v], v] for v in range(n) if weight[start][v] is not None and v in not_added]:
        edges.put(e)


def extract_maximum(edges):
    return edges.get()


n, m, weight = input_data()
maximum_spanning_tree = []
added = set()
not_added = set([x for x in range(n)])
edges = PriorityQueue()
v = 0
add_vertex(v, edges, weight)
while len(not_added) != 0 and not edges.empty():
    e = extract_maximum(edges)
    if e[1] in not_added:
        maximum_spanning_tree.append(e[0])
        add_vertex(e[1], edges, weight)
if len(not_added) > 0:
    print("Oops! I did it again")
else:
    print(-1 * sum(maximum_spanning_tree))
