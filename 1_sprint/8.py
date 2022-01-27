x = str(input())
y = str(input())

if (len(y) > len(x)):
    tmp = x
    x = y
    y = tmp

buf=0
res=""
for i in range(len(x)+1):
    if i < len(y):
        tmp = int(x[-1-i]) + int(y[-1-i]) + buf
        if tmp == 3:
            buf = 1
            res = "1" + res
        elif tmp == 2:
            buf = 1
            res = "0" + res
        else:
            buf = 0
            res = str(tmp) + res
    elif i < len(x):
        tmp = int(x[-1 - i]) + buf
        if tmp == 2:
            buf = 1
            res = "0" + res
        else:
            buf = 0
            res = str(tmp) + res
    elif i == len(x) and buf == 1:
        res = "1" + res
print(res)