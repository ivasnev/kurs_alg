n = int(input())
dic = {}
for _ in range(n):
    inp = input().split(" ")
    if inp[4] == "B":
        continue
    if dic.get(int(inp[3])) is None:
        dic[int(inp[3])] = [(int(inp[0]), int(inp[1]), int(inp[2]), inp[4])]
    else:
        dic[int(inp[3])].append((int(inp[0]), int(inp[1]), int(inp[2]), inp[4]))
for key in dic.keys():
    dic[key].sort(key=lambda x: (x[0], x[1], x[2]))
    time = 0
    for i in range(0, len(dic[key]), 2):
        start = dic[key][i]
        end = dic[key][i + 1]
        time += (end[0]*1440 + end[1]*60 + end[2]) - (start[0]*1440 + start[1]*60 + start[2])
    dic[key] = str(time)
dic = list(dic.items())
dic.sort(key=lambda x: x[0])
for elem in dic:
    print(elem[1], end=" ")
