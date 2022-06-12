n = int(input())
works = {}
works_lim = {}
for _ in range(n):
    inp = input().split(",")
    works_lim[inp[0]] = int(inp[1])
    works[inp[0]] = []

m = int(input())
for _ in range(m):
    worker = input().split(",")
    worker[2] = int(worker[2])
    worker[3] = int(worker[3])
    works[worker[1]].append(worker)

for key, elem in works.items():
    elem.sort(key=lambda x: (-x[2], x[3]))
    elem[:] = elem[:works_lim[key]]

guys = []
for key, elem in works.items():
    for i in elem:
        guys.append(i[0])
guys.sort()
print("\n".join(guys))
