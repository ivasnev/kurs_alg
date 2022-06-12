def main():
    f = open('input.txt', 'r')
    res = []
    ind = 1
    s = f.read(1)
    while s != '\n':
        simb_bef = ""
        cur = 0
        l_l = [False, -1]
        fi_r = [False, -1]
        c = {"(": 0, ")": 0}
        f_l = -1
        f_r = -1
        while s != "=" and s != '\n':
            if c["("] == c[")"]:
                c = {"(": 0, ")": 0}
                f_l = -1
                f_r = -1
            if s == "(":
                if f_l == -1:
                    f_l = ind
                c["("] += 1
            elif s == ")":
                if cur == 0:
                    c[")"] -= 1
                    l_l[1] = ind
                    l_l[0] = True
                if f_r == -1:
                    f_r = ind
                c[")"] += 1
            ind += 1
            cur += 1
            simb_bef = s
            s = f.read(1)
        if simb_bef == "(":
            c["("] -= 1
            fi_r[1] = ind-1
            fi_r[0] = True
        a = c["("] - c[")"]
        if abs(a) == 1:
            if a > 0 and not fi_r[0] and not l_l[0]:
                res.append(f_l)
            elif a < 0 and not fi_r[0] and not l_l[0]:
                res.append(f_r)
        elif abs(a) == 0 and (fi_r[0] or l_l[0]) and not (fi_r[0] and l_l[0]):
            if fi_r[0]:
                res.append(fi_r[1])
            else:
                res.append(l_l[1])
        if s == "=":
            ind += 1
            cur += 1
            simb_bef = s
            s = f.read(1)

    if len(res) != 1:
        print(-1)
    else:
        print(res[0])


main()
