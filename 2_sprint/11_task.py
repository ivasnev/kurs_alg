alCalc = {0: 1, 1: 1}


def fib(n):
    if alCalc.get(n) == None:
        alCalc[n] = fib(n - 1) + fib(n - 2)
    return alCalc[n]


print(fib(int(input())))
