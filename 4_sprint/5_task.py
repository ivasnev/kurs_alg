str = list(input())
n= len(str)
if n != 0:
    max = 0
    for i in range(n):
        dict = {}
        tmp_max = 0
        for j in range(i, n):
            if n - j + tmp_max < max:
                break
            if not(dict.get(str[j])):
                dict[str[j]] = 1
                tmp_max += 1
            else:
                break
        if max < tmp_max: max = tmp_max
    print(max)
else:
    print(0)