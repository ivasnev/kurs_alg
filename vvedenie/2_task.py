n = int(input())
array = list(map(int, input().strip().split()))
k = int(input())
cur_sum = 0
result = []
for i in range(n-k+1):
    if i == 0:
        for j in range(k):
            cur_sum += array[j]
    else:
        cur_sum -= array[i-1]
        cur_sum += array[i+k-1]
    result.append(cur_sum/k)

print(" ".join(map(str, result)))