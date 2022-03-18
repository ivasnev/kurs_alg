def f(n, k, stack):
    if stack[n] is not None:
        return stack[n]
    if n-k-1 > 0:
        a = stack[n-k-1]
    else:
        a = 0
    su = 2*stack[n-1] - a
    stack[n] = su
    return su


n_i, k_i = map(int, input().split())
stack_i = [None for _ in range(n_i + 2)]
stack_i[0] = 0
stack_i[1] = 1
stack_i[2] = 1
for i in range(3, n_i):
    f(i, k_i, stack_i)
print(f(n_i, k_i, stack_i) % (10**9 + 7))

