def main():
    f = open('input.txt', 'r')
    res = []
    ind = 1
    s = f.read(1)
    while s != '\n':
        c = {"(": 0, ")": 0}
        simb_bef = ""
        f_l = -1
        f_r = -1
        l_l = [False, -1]
        fi_r = [False, -1]
        while s != "=" and s != '\n':
            if s == "(":
                if c["("] - c[")"] == 0:
                    f_l = ind
                c["("] += 1
            elif s == ")":
                if f_l == f_r == -1:
                    l_l[1] = ind
                    l_l[0] = True
                if f_r == -1:
                    f_r = ind
                c[")"] += 1
            ind += 1
            simb_bef = s
            s = f.read(1)
        if simb_bef == "(":
            fi_r[1] = ind-1
            fi_r[0] = True
        a = c["("] - c[")"]
        if abs(a) == 1:
            if a > 0:
                if fi_r[0]:
                    res.append(fi_r[1])
                else:
                    res.append(f_l)
            else:
                if l_l[0]:
                    res.append(l_l[1])
                else:
                    res.append(f_r)
        if s == "=":
            ind += 1
            simb_bef = s
            s = f.read(1)

    if len(res) != 1:
        print(-1)
    else:
        print(res[0])


main()
