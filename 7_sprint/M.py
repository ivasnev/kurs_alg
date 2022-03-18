from random import randint


def rand_d():
    nf, mf = 100, 1000
    cost_f = [0 for _ in range(nf)]
    weight_f = [0 for _ in range(nf)]
    for i in range(nf):
        weight_f[i], cost_f[i] = map(int, input().split())
    dp = [[0 for _ in range(mf)], [0 for _ in range(mf)]]
    return nf, mf, cost_f, weight_f, dp


def Inp_d():
    nf, mf = map(int, input().split())
    cost_f = [0 for _ in range(nf)]
    weight_f = [0 for _ in range(nf)]
    for i in range(nf):
        weight_f[i], cost_f[i] = map(int, input().split())
    dp = [[0 for _ in range(mf)], [0 for _ in range(mf)]]
    return nf, mf, cost_f, weight_f, dp


def main():
    n, m, cost, weight, dp = Inp_d()
    for i in range(n):
        for j in range(m):
            if j - weight[i] > -1:
                a = cost[i] + dp[0][j - weight[i]]
                if a < dp[0][j]:
                    a = dp[0][j]
            else:
                a = cost[i]
                if a < dp[0][j]:
                    a = dp[0][j]
            if a <= j:
                dp[1][j] = a
        dp[0] = dp[1].copy()
    print(dp[1][m - 1])


if __name__ == "__main__":
    main()
