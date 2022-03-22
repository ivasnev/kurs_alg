from collections import Counter


def all_palindromes2(string: str):
    freq = sorted(Counter(string).items())
    half = ''.join(n // 2 * x for x, n in freq)
    middle = next((x for x, n in freq if n % 2 == 1), '')
    return half + middle + half[::-1]


print(all_palindromes2(input()))
