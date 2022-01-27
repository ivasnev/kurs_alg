from collections import Counter

def pr():
    n = int(input())
    if n == 0:
        print("0")
        return
    else:
        arr = list(map(int, input().split()))
        D = Counter(arr)
        max_in_best = min(D.values()) * 2
        if len(D) == 1:
            print("0")
            return
        arr_left = [(0, 0)]
        c_0 = 0
        c_1 = 0
        for i in arr:
            if i == 0:
                c_0 += 1
            else:
                c_1 += 1
            arr_left.append((c_0, c_1))
        for i in range(max_in_best, 1, -1):
            left = 1
            right = left + i - 1
            left -= 1
            for j in range(n - i + 1):
                if arr_left[right][0] - arr_left[left][0] == arr_left[right][1] - arr_left[left][1]:
                    print(right - left)
                    return
                else:
                    left += 1
                    right += 1
        print("0")


def pr2():
    n = int(input())
    if n == 0:
        print("0")
        return
    else:
        arr = list(map(int, input().split()))
        D = Counter(arr)
        max_in_best = min(D.values()) * 2
        if len(D) == 1:
            print("0")
            return
        arr_resized = [[arr[0],0]]

        for i in arr:
            if i == arr_resized[-1][0]:
                arr_resized[-1][1] += 1
            else:
                arr_resized.append([i, 1])

        arr_left = [(0, 0)]
        c_0 = 0
        c_1 = 0
        for i in arr_resized:
            if i[0] == 0:
                c_0 += i[1]
            else:
                c_1 += i[1]
            arr_left.append((c_0, c_1))
        print(arr_resized)
        print(arr_left)

pr2()