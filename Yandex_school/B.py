n = int(input())
works = {}
works_lim = {}
for _ in range(n):
    inp = input().split(",")
    works_lim[inp[0]] = int(inp[1])
    works[inp[0]] = []

n = int(input())
for _ in range(n):
    worker = input().split(",")
    worker[2] = int(worker[2])
    worker[3] = int(worker[3])
    work = works.get(worker[1])
    si = len(work)
    cur_name = worker[1]
    cur_task = worker[2]
    cur_ex = worker[3]
    if si < works_lim.get(cur_name):
        work.append(worker)
        if si+1 == works_lim.get(worker[1]):
            work.sort(key=lambda x: (-x[2], x[3]))

    elif cur_task > work[-1][2] or (cur_task == work[-1][2] and cur_ex < work[-1][3]):
        left, right = 0, si - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if cur_task > work[pivot][2] or (cur_task == work[pivot][2] and cur_ex < work[pivot][3]):
                right = pivot - 1
            else:
                left = pivot + 1
        works[cur_name] = []
        for i in range(right+1):
            works[cur_name].append(work[i])
        works[cur_name].append(worker)
        for i in range(right+1, si-1):
            works[cur_name].append(work[i])

guys = []
for key, elem in works.items():
    for i in elem:
        guys.append(i[0])
guys.sort()
print("\n".join(guys))
