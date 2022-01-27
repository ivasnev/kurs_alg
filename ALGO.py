def eratosthenes_effective(n): #самый быстрый метод для простых вызывать от корень(n)
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(num * num, n + 1, num):
                numbers[j] = False
    return numbers


def get_least_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return primes, lp

alf = "0123456789ABCDEF"


def ten_to_num(x, base):
    res = ""
    if x == 0: return "0"
    num = x
    while num > 0:
        res = alf[num % base] + res
        num = int(num / base)
    return res


def num_to_ten(x, base):
    res = 0
    for i in range(len(x)):
        res += alf.find(x[i]) * (base ** (len(x) - i - 1))
    return res

def generate(cur, open, closed, n): #start generate("", 0, 0, n) правильная скобочная послед
    if len(cur) == 2 * n:
        print(cur)
        return
    if open < n:
        generate(cur + "(", open + 1, closed, n)
    if closed < open:
        generate(cur + ")", open, closed + 1, n)

alCalc = {0: 1, 1: 1}

def fib(n):
    if alCalc.get(n) == None:
        alCalc[n] = fib(n - 1) + fib(n - 2)
    return alCalc[n]


def iterativeFib(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a



