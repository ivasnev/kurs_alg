# ID 66448395
# Временная сложность депакера O(N), где N количество символов строке исходнике
# Временная сложность функции водителя O(M), где M количество символов в самой маленькой строке
# Общая временная сложность O(N*F), где F колличество входных строк


import sys

sys.setrecursionlimit(100000)

# Реализация стека вызовов делает код данной задачи не просто грамоздким, но и вообще не очевидным,
# глубина рекурсии из ограничений тз не может быть ОЧЕНЬ большой
# Я попробовал его реализовать но получилось ужасно, времени на дальнейшую разработку стека нет
# Из-за прошлых фин задач у меня осталось 2 ДНЯ до конца курса, чтобы закрыть эти две задачи


def depacker(s: str) -> str:
    if s[0] == "[":
        s = s[1:]
    res = ""
    tmp_str = ""
    n = ""
    kol_l = 0
    kol_j = 0
    flag = True
    for i in range(len(s)):
        tmp_item = s[i]
        if tmp_item.isdigit() and flag:
            n += tmp_item
        elif tmp_item == "[":
            flag = False
            tmp_str += tmp_item
            kol_l += 1
        elif tmp_item == "]":
            kol_j += 1
            if kol_l == kol_j:
                d = depacker(tmp_str)
                res += int(n) * d
                flag = True
                tmp_str = ""
                n = ""
                kol_l = 0
                kol_j = 0
            else:
                tmp_str += tmp_item
        elif flag:
            res += tmp_item
        else:
            tmp_str += tmp_item
    res += tmp_str
    return res
            

def main():
    n = int(input())
    mi = depacker(input())
    ma = mi
    for _ in range(n-1):
        inp = depacker(input())
        if inp > ma:
            ma = inp
        if inp < mi:
            mi = inp
    res = ""
    for i in range(len(mi)):
        if mi[i] == ma[i]:
            res += mi[i]
        else:
            break
    print(res)


if __name__ == '__main__':
    main()
