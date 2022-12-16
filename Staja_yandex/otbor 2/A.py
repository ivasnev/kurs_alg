n = int(input())
for _ in range(n):
    inp = input().split(",")
    a = set()
    for i in range(3):
        for elem in set(list(inp[i])):
            a.add(elem)
    a = len(a)
    b = sum([int(x) for x in inp[3]+inp[4]]) * 64
    c = (ord(inp[0][0].upper())-64) * 256
    cur_res = hex(a+b+c).split('x')[-1]
    cur_res = cur_res[-3::].upper()
    cur_res = "0"*(3 - len(cur_res)) + cur_res
    print(cur_res, end=' ')
