def generate(cur, open, closed, n):
    if len(cur) == 2 * n:
        print(cur)
        return
    if open < n:
        generate(cur + "(", open + 1, closed, n)
    if closed < open:
        generate(cur + ")", open, closed + 1, n)

n = int(input())
generate("", 0, 0, n)