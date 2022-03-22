import sys


def find(pat, text):
    result = []
    s = pat + '#' + text
    p = [0 for _ in range(len(s))]
    p_prev = 0
    for i in range(1, len(s)):
        k = p_prev
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        if i < len(pat):
            p[i] = k
        p_prev = k
        if k == len(pat):
            result.append(i - 2 * len(pat))
    return result


def main():
    try:
        text = input()
        pattern = input()
        replace = input()
        if len(replace) == 0 or len(pattern) == 0:
            print(text)
            return
        arr = find(pattern, text)
        s_t = text[:arr[0]]
        for i in range(len(arr) - 1):
            s_t += replace + text[arr[i]+len(pattern):arr[i + 1]]
        s_t += replace + text[arr[-1]+len(pattern):]
        print(s_t)
    except Exception:
        print(sys.exc_value)



if __name__ == "__main__":
    main()