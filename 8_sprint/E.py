s = input()
n = int(input())
arr = []
for _ in range(n):
    a = input().split()
    arr.append([a[0], int(a[1])])
arr.sort(key=lambda x: x[1])
s_t = s[:arr[0][1]]
for i in range(len(arr)-1):
    s_t += arr[i][0] + s[arr[i][1]:arr[i+1][1]]
s_t += arr[n-1][0] + s[arr[n-1][1]:]
print(s_t)
