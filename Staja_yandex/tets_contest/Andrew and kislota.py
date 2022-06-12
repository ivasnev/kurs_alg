def main():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        if i and arr[i - 1] > arr[i]:
            print(-1)
            return
    print(arr[n - 1] - arr[0])


main()
