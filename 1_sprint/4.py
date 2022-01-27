n = int(input())
array = list(map(int, input().strip().split()))
hao_counter = 0
for i in range(n):
    if i - 1 >= 0 and i+1 < n:
        if array[i-1] < array[i] and array[i] > array[i+1]:
            hao_counter += 1
    elif i - 1 >= 0:
        if array[i-1] < array[i]:
            hao_counter += 1
    elif i+1 < n:
        if array[i] > array[i+1]:
            hao_counter += 1
    else:
        hao_counter += 1
print(hao_counter)