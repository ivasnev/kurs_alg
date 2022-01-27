n = int(input())
arr = [int(x) if x == '1' else -1 for x in input().split()]
c_0 = 0
c_1 = 0
for i in range(n-1):
    arr[i+1] = arr[i]+arr[i+1]
print(arr)