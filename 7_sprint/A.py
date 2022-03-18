def birga():
    n = int(input())
    if n < 2:
        print(0)
    inp_a = list(map(int, input().split()))
    list_of_ex = [inp_a[0],inp_a[1]]
    rise = False
    start_stat = 2
    if inp_a[0] < inp_a[1]:
        rise = True
        start_stat = 1
    for tmp_i in inp_a[2:]:
        if rise:
            if list_of_ex[-1] < tmp_i:
                list_of_ex[-1] = tmp_i
            else:
                list_of_ex.append(tmp_i)
                rise = False
        else:
            if list_of_ex[-1] > tmp_i:
                list_of_ex[-1] = tmp_i
            else:
                list_of_ex.append(tmp_i)
                rise = True
    # print(list_of_ex)
    sum = 0
    for i in range(start_stat,len(list_of_ex),2):
        sum += list_of_ex[i] - list_of_ex[i-1]
    print(sum)



birga()
