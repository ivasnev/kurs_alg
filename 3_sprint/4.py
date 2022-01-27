n = int(input())
arr_1 = list(map(int,input().split()))
m = int(input())
arr_2 = list(map(int,input().split()))
arr_1.sort()
arr_2.sort()
counter = 0
ind_1 = 0
ind_2 = 0
while(True):
    if ind_1 == n or ind_2 == m:
        break
    if arr_1[ind_1] > arr_2[ind_2]:
        ind_2 += 1
    else:
        counter += 1
        ind_1 += 1
        ind_2 += 1
print(counter)