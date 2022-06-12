# array = [4,3,2,3,2,1,5,6,7,5,9]
# n = len(array)
def task():
    n = 4
    array = [10,9,8,7]
    if n == 1:
        print(0)
    a = array[0]
    b = array[1]
    counter = 2
    if a < b:
        rise = True
    else:
        rise = False
    res = 0
    min_cur = min(a,b)
    max_cur = max(a,b)
    for _ in range(n-2):
        tmp = array[counter]
        counter += 1
        if rise:
            if max_cur > tmp:
                rise = False
                res += max_cur - min_cur
                print(max_cur, min_cur)
                min_cur = tmp
            else:
                max_cur = tmp
        else:
            if min_cur < tmp:
                rise = True
                max_cur = tmp
            else:
                min_cur = tmp
    if rise:
        res += max_cur - min_cur
        print(max_cur, min_cur)
    print(res)

task()
