from collections import Counter


def main():
    f = open('input.txt', 'r')
    s = f.readline()
    ind = s.find("=")
    if ind != -1:
        arr = s.split("=")
        inds = []
        for i in range(len(arr)):
            c = Counter(arr[i])
            a = c["("] - c[")"]
            if abs(a) == 1:
                inds.append([i, a])
        if len(inds) != 1:
            print(-1)
        else:
            ind = s.find(arr[inds[0][0]])
            if inds[0][1] > 0:
                print(s.find("(", ind, ind + len(arr[inds[0][0]]) + 1) + 1)
            else:
                print(s.find(")", ind, ind + len(arr[inds[0][0]]) + 1) + 1)
    else:
        c = Counter(s)
        a = c["("] - c[")"]
        if abs(a) == 1:
            if a > 0:
                print(s.find("(") + 1)
            else:
                print(s.find(")") + 1)
        else:
            print(-1)


main()
