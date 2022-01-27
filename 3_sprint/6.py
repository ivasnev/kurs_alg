def checker(arr):
    maxi = 0
    n = len(arr)
    arr.sort(reverse=True)
    for i in range(0, n - 2):
        if arr[i] < (arr[i + 1] + arr[i + 2]):
            maxi = max(maxi, arr[i] + arr[i + 1] + arr[i + 2])
            break
    if (maxi == 0):
        return "None"
    else:
        return str(maxi)


n = int(input())
arr = list(map(int, input().split()))
print(checker(arr))