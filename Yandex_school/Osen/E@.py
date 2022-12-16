def checker(ind_skip, _s_f):
    ind = 1
    stack = []
    is_good = True
    for s in _s_f:
        if ind_skip == ind:
            ind += 1
            continue
        if s == '{':
            stack.append(s)
        elif s in '}':
            if not stack:
                is_good = False
                break
            open_bracket = stack.pop()
            if open_bracket == "{" and s == "}":
                ind += 1
                continue
            is_good = False
            break
        ind += 1
    return is_good and len(stack) == 0


f = open('input.txt', 'r')
s_f = f.readline()
depth = 0
first_close_id = -1
open_brackets_id = -1
ind = 1
for s in s_f:
    if s == "}":
        if first_close_id == -1:
            first_close_id = ind
        depth -= 1
    if s == "{":
        if depth == 0:
            open_brackets_id = ind
        depth += 1
    ind += 1
f.close()
if depth == 1:
    num = open_brackets_id
    if checker(num, s_f):
        print(num)
    else:
        print(-1)
elif depth == -1:
    num = first_close_id
    if checker(num, s_f):
        print(num)
    else:
        print(-1)
else:
    print(-1)
