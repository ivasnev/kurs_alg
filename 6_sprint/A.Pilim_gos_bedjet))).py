# ID 65681787
# Временная сложность O(E⋅logV), где E — количество рёбер в графе, а V — количество вершин
# Скорость поиска max O(1) благодаря приор. очереди. шагов требуется по кол рёбер
# Сложность по памяти мы имеем 2 сета в сумме дающие V элементов, матрицу связи с весами размера V^2,
# и приор. очеред. или древо хранящая рёбра в худшем случае V-1 ребро следовательно сложность по памяти,
# будет O(V^2)
#

from queue import PriorityQueue


def input_data():
    n_f, m_f = map(int, input().split())
    weight_f = [[None for _ in range(n_f)] for _ in range(n_f)]
    for i in range(m_f):
        a, b, c = map(int, input().split())
        if weight_f[a - 1][b - 1] is None or -1 * weight_f[a - 1][b - 1] < c:
            weight_f[a - 1][b - 1] = -c
            weight_f[b - 1][a - 1] = -c
    return n_f, m_f, weight_f


def add_vertex(start, edges_f, weight_f, added_f, not_added_f, n_f):
    added_f.add(start)
    not_added_f.remove(start)
    for e_f in [[weight_f[start][v_f], v_f] for v_f in range(n_f) if
                weight_f[start][v_f] is not None and v_f in not_added_f]:
        edges_f.put(e_f)


def extract_maximum(edges_f):
    return edges_f.get()


def main():
    n, m, weight = input_data()
    maximum_spanning_tree = []
    added = set()
    not_added = set([x for x in range(n)])
    edges = PriorityQueue()
    v = 0
    add_vertex(v, edges, weight, added, not_added, n)
    while len(not_added) != 0 and not edges.empty():
        e = extract_maximum(edges)
        if e[1] in not_added:
            maximum_spanning_tree.append(e[0])
            add_vertex(e[1], edges, weight, added, not_added, n)
    if len(not_added) > 0:
        print("Oops! I did it again")
    else:
        print(-1 * sum(maximum_spanning_tree))


main()
