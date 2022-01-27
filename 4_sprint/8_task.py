dict_1 = {}
str_1 = input()
str_2 = input()
if len(str_1) == len(str_2):
    flag = True
    for x in range(len(str_1)):
        if dict_1.get(str_1[x]):
            if str_2[x] != dict_1.get(str_1[x]):
                flag = False
                break
        else:
            dict_1[str_1[x]] =str_2[x]
    arr_1 = list(dict_1.items())
    arr_1.sort(reverse=True, key=lambda x: x[1])
    for i in range(len(arr_1) - 1):
        if arr_1[i][1] == arr_1[i + 1][1]:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
