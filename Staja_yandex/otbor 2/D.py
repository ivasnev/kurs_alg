def first(start, end, sorted_start, start_suf_sum):
    ind_s = ind_e = -1
    for i, elem in enumerate(sorted_start):
        if elem >= start and ind_s == -1:
            ind_s = i
        if elem <= end:
            ind_e = i
    if ind_e == len(sorted_start) - 1:
        return start_suf_sum[ind_s]
    if ind_s <= ind_e:
        return start_suf_sum[ind_s] - start_suf_sum[ind_e + 1]
    return 0


def second(start, end, sorted_end, end_pref_sum):
    ind_s = ind_e = -1
    for i, elem in enumerate(sorted_end):
        if elem >= start and ind_s == -1:
            ind_s = i
        if elem <= end:
            ind_e = i
    if ind_e == len(sorted_end) - 1:
        return end_pref_sum[ind_e]
    if ind_s <= ind_e:
        return end_pref_sum[ind_e] - end_pref_sum[ind_s - 1]
    return 0


n = int(input())
dic_start = {}
dic_end = {}
for i in range(n):
    inp = [int(x) for x in input().split(" ")]
    if dic_start.get(inp[0]) is None:
        dic_start[inp[0]] = [(inp[1] - inp[0], inp[2])]
    else:
        dic_start[inp[0]].append((inp[1] - inp[0], inp[2]))
    if dic_end.get(inp[1]) is None:
        dic_end[inp[1]] = [inp[1] - inp[0]]
    else:
        dic_end[inp[1]].append(inp[1] - inp[0])
unic_start = len(dic_start)
unic_end = len(dic_end)
start_suf_sum = [0] * unic_start
end_pref_sum = [0] * unic_end
sorted_start = list(dic_start.keys())
sorted_start.sort()
sorted_end = list(dic_end.keys())
sorted_end.sort()
for i, key in enumerate(sorted_start):
    start_suf_sum[i] = sum([x[1] for x in dic_start[key]])
for i in range(unic_start - 2, -1, -1):
    start_suf_sum[i] += start_suf_sum[i + 1]
for i, key in enumerate(sorted_end):
    end_pref_sum[i] = sum(dic_end[key])
for i in range(1, unic_end):
    end_pref_sum[i] += end_pref_sum[i - 1]


q = int(input())
for i in range(q):
    inp = list(map(int, input().split()))
    if inp[2] == 1:
        print(first(inp[0], inp[1], sorted_start, start_suf_sum), end=" ")
    else:
        print(second(inp[0], inp[1],sorted_end,end_pref_sum), end=" ")
