n, m = map(int,input().split())
arr_1 = list(map(int,input().split()))
arr_1.sort()
counter = 0
cur_s = 0
ind_1 = 0
while(True):
    if ind_1 == n or cur_s + arr_1[ind_1] > m:
        break
    else:
        cur_s += arr_1[ind_1]
        counter += 1
        ind_1 += 1
print(counter)