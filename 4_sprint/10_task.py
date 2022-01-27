n = int(input())
S = int(input())

if n >= 1:
    array = [int(x) for x in input().split()]
    if n >= 4:
        array.sort()
        ans = []
        d = dict()

        for i in range(n - 1):
            for j in range(i + 1, n):
                try:
                    d[array[i] + array[j]].append([i, j])
                except KeyError:
                    d[array[i] + array[j]] = [[i, j]]

        for z in d.keys():
            x = S - z
            try:
                if d[x]:
                    for r in d[z]:
                        for k in d[x]:
                            if k[0] > r[1]:
                                t = [array[r[0]], array[r[1]], array[k[0]], array[k[1]]]
                                if t not in ans:
                                    ans.append(t)
            except KeyError:
                continue

        print(len(ans))
        ans.sort()
        for i in range(len(ans)):
            print(' '.join(list(map(str, ans[i]))))
    else:
        print(0)
else:
    print(0)