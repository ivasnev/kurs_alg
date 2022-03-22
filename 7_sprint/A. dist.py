# ID 66200689
# Алгоритм Левейнштейна работает за О(N*M) по времени,
# и за O(2M) по памяти


def alg_levin(x, y):
    def m(s1, s2):
        if s1 == s2:
            return 0
        return 1

    d = [[i for i in range(len(y) + 1)],
         [0 for _ in range(len(y) + 1)]]
    ind = 1
    for i in range(1, len(x) + 1):
        d[ind][0] = d[ind-1][0] + 1
        for j in range(1, len(y) + 1):
            d[ind][j] = min(d[ind-1][j] + 1,
                            d[ind][j - 1] + 1,
                            d[ind-1][j - 1] + m(x[i - 1], y[j - 1]))
        ind = (ind + 1) % 2
    return d[(ind + 1) % 2][-1]


def main():
    str_1 = input()
    str_2 = input()
    print(alg_levin(str_1, str_2))


if __name__ == '__main__':
    main()