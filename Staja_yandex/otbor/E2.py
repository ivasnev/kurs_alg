def intersection(fir_rec, sec_rec):
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
a = []
for i in range(n):
    inp = list(map(int, input().split()))
    a.append(((inp[0], inp[1]), "l", i, (inp[0], inp[1], inp[2], inp[3])))
    a.append(((inp[2], inp[3]), "r", i, (inp[0], inp[1], inp[2], inp[3])))
a.sort(key=lambda x: x[0][1])
rec = [set() for _ in range(n)]
for i in range(2 * n):
    if a[i][1] == "l":
        for tmp_i in range(i + 1, 2 * n):
            if a[tmp_i][2] == a[i][2]:
                break
            if a[i][3][1] <= a[tmp_i][3][3] or a[tmp_i][3][1] <= a[i][3][3]:
                continue
            else:
                rec[a[i][2]].add(a[tmp_i][2])
                rec[a[tmp_i][2]].add(a[i][2])
for a in rec:
    print(len(a), end=" ")
