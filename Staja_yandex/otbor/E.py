class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rec:
    def __init__(self, x1, y1, x2, y2, ind):
        self.edges = []
        self.ind = ind
        self.point_l_top = Point(x1, y2)
        self.point_l_bottom = Point(x1, y1)
        self.point_r_top = Point(x2, y2)
        self.point_r_bottom = Point(x2, y1)

    def ret_e(self):
        return [self.point_l_top, self.point_l_bottom, self.point_r_top, self.point_r_bottom]

    def intersection(self, sec_rec):
        if sec_rec in self.edges:
            return
        l_1, r_1 = self.point_l_top, self.point_r_bottom
        l_2, r_2 = sec_rec.point_l_top, sec_rec.point_r_bottom
        if (l_1.x >= r_2.x or l_2.x >= r_1.x):
            return
        if (l_1.y <= r_2.y or l_2.y <= r_1.y):
            return
        self.edges.append(sec_rec)


n = int(input())
rec = []
d = {}
for i in range(n):
    d[i] = []
for i in range(n):
    inp = list(map(int, input().split()))
    rec.append(Rec(inp[0], inp[1], inp[2], inp[3], i))
rec.sort(key=lambda r: r.point_l_top.x)
for i in range(n):
    for x in range(n):
        if rec[x].point_l_top.x > rec[i].point_r_top.x:
            break
        if x == i:
            continue
        rec[i].intersection(rec[x])
rec.sort(key=lambda r: r.ind)
for a in rec:
    print(len(a.edges), end=" ")
