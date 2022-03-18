from random import randint


def rand_d():
    nf, mf = 1000, 9999
    mf += 1
    arr = [randint(0, mf - 1) for _ in range(nf)]
    dp = [[0 for _ in range(mf)], [0 for _ in range(mf)]]
    return nf, mf, arr, dp


def Inp_d():
    nf, mf = map(int, input().split())
    mf += 1
    arr = list(map(int, input().split()))
    dp = [[0 for _ in range(mf)], [0 for _ in range(mf)]]
    return nf, mf, arr, dp


def main():
    n, m, inp_arr, dp = Inp_d()
    for item in inp_arr:
        for j in range(item, m):
            if j - item > -1:
                a = item + dp[0][j - item]
                if a < dp[0][j]:
                    a = dp[0][j]
            else:
                if dp[0][j] > item:
                    a = dp[0][j]
                else:
                    a = item
            if a <= j:
                dp[1][j] = a
        dp[0] = dp[1].copy()
    print(dp[1][m-1])


if __name__ == "__main__":
    main()
