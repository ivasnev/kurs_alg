alf = "0123456789ABCDEF"


def ten_to_num(x, base):
    res = ""
    if x == 0: return "0"
    num = x
    while num > 0:
        res = alf[num % base] + res
        num = int(num / base)
    return res


x = int(input())
print(ten_to_num(x, 2))
