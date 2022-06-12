from random import randint
# n = 1000
# array = [randint(-10**9, 10*9) for _ in range(n)]
n = int(input())
array = list(map(int, input().split()))


pol = []
otr = []
nul = False

for elem in array:
    if elem > 0:
        pol.append(elem)
    elif elem == 0:
        nul = True
    else:
        otr.append(elem)
if len(otr) % 2 != 0 and len(otr) != 0:
    print(max(otr))
else:
    if nul:
        print(0)
    else:
        if len(pol) != 0:
            print(min(pol))
        else:
            print(min(otr))
