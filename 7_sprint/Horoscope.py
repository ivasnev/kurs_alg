def lcs_length(x, y):
    curr = [0]*(1 + len(y))
    for x_elem in x:
        prev = curr[:]
        for y_i, y_elem in enumerate(y):
            if x_elem == y_elem:
                curr[y_i + 1] = prev[y_i] + 1
            else:
                curr[y_i + 1] = max(curr[y_i], prev[y_i + 1])
    return curr


def LCS_HIRSHBERG(x, y):
    x_len = len(x)
    if x_len == 0:
        return []
    elif x_len == 1:
        if x[0] in y:
            return [x[0]]
        else:
            return []
    else:
        i = x_len // 2
        xb, xe = x[:i], x[i:]
        L1 = lcs_length(xb, y)
        L2 = reversed(lcs_length(xe[::-1], y[::-1]))
        SUM = (l1 + l2 for l1,l2 in zip(L1, L2))
        _, j = max((sum_val, sum_i) for sum_i, sum_val in enumerate(SUM))
        yb, ye = y[:j], y[j:]
        return LCS_HIRSHBERG(xb, yb) + LCS_HIRSHBERG(xe, ye)


def main():
    n = int(input())
    x = input().split()
    m = int(input())
    y = input().split()
    arr = LCS_HIRSHBERG(x, y)
    ind = 0
    print(len(arr))
    for i in arr:
        while x[ind] != i:
            ind += 1
        print(ind+1, end=" ")
        ind += 1
    print()
    ind = 0
    for i in arr:
        while y[ind] != i:
            ind += 1
        print(ind+1, end=" ")
        ind += 1


if __name__ == '__main__':
    main()
