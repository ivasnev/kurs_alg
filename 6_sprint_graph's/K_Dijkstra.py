from collections import deque


def Dijkstra(s, weight):
    def relax(u, v):
        if dist[v] > dist[u] + weight[u][v]:
            dist[v] = dist[u] + weight[u][v]
            previous[v] = u

    def get_min_dist_not_visited_vertex():
        current_minimum = float("inf")
        current_minimum_vertex = None
        for v in range(n):
            if not visited[v] and dist[v] < current_minimum:
                current_minimum = dist[v]
                current_minimum_vertex = v
        return current_minimum_vertex

    def outgoing_edges(u):
        out_edges = []
        for v in range(n):
            if weight[u][v] is not None:
                out_edges.append(v)
        return out_edges

    dist = [float("inf")] * n
    previous = [None] * n
    visited = [False] * n
    dist[s] = 0
    flag = True
    while flag:
        u = get_min_dist_not_visited_vertex()
        visited[u] = True
        neighbours = outgoing_edges(u)
        for v in neighbours:
            relax(u,v)
        flag = False
        for v in range(n):
            if not visited[v] and dist[v] != float("inf"):
                flag = True
                break
    for v in range(n):
        if dist[v] == float("inf"):
            dist[v] = -1
    return dist




n, m = map(int, input().split())
list_of_dist = [[None for y in range(n)] for x in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    if list_of_dist[a - 1][b - 1] is None or list_of_dist[a - 1][b - 1] > c:
        list_of_dist[a - 1][b - 1] = c
        list_of_dist[b - 1][a - 1] = c

for i in range(n):
    print(" ".join(map(str, Dijkstra(i, list_of_dist))))

