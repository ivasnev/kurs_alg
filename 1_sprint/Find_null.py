#id 58822007
n = int(input())
d = 0
array_input = [int(x) for x in input().split()]
finalArray = [0 for x in range(n)]
ind_l = 0
while array_input[ind_l] != 0:
    ind_l += 1
for i in range(ind_l, n):
    if array_input[i] == 0:
        finalArray[i] = 0
    else:
        finalArray[i] = finalArray[i - 1] + 1

ind_r = n - 1
while array_input[ind_r] != 0:
    ind_r -= 1
for i in range(ind_r, -1, -1):
    if array_input[i] == 0:
        finalArray[i] = 0
    else:
        finalArray[i] = min(finalArray[i], finalArray[i + 1] + 1)
for i in range(ind_l - 1, -1, -1):
    finalArray[i] = finalArray[i + 1] + 1

for i in finalArray:
    print(i,end=' ')

