# ID 66242983
# Сложность по времени О(M*N), где N колличество монет, M размер кучки
# Сложность по памяти О(M), M размер кучки

def same_sum():
    n = int(input())
    inp_arr = list(map(int, input().split()))
    d = {}
    for item in inp_arr:
        if d.get(item):
            d[item] += 1
        else:
            d[item] = 1
    tmp = []
    m = 0
    for item in d.items():
        if item[1] % 2 == 1:
            tmp.append(item[0])
            m += item[0]
    if m % 2 == 1:
        print(False)
        return
    m = m // 2
    dp = [[0 for _ in range(m+1)], [0 for _ in range(m+1)]]
    old = 0
    new = 1
    for i in range(len(inp_arr)):
        item = inp_arr[i]
        for j in range(m+1):
            if j - item >= 0:
                a = item + dp[old][j - item]
                if a < dp[old][j]:
                    a = dp[old][j]
            else:
                if dp[old][j] > item:
                    a = dp[old][j]
                else:
                    a = item
            if a <= j:
                dp[new][j] = a
            else:
                dp[new][j] = dp[old][j]
        old, new = new, old

    print(m == dp[new][-1])


if __name__ == "__main__":
    same_sum()
