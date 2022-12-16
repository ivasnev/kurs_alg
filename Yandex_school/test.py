# def checker(exp, ind):
#     t = []
#     for i, s in enumerate(exp, ind):
#         if s == '}' and t and t[-1][1] == '{':
#             t.pop()
#         elif s in '{}':
#             t.append((i, s))
#     return t[0][0] if len(t) == 1 else -1
#
# f = open('input.txt', 'r')
# s = f.readline()
# res = []
# ind = 1
# for elem in s.split("="):
#     ret = checker(elem, ind)
#     ind += len(elem) + 1
#     if ret != -1:
#         res.append(ret)
#     if len(res) == 2:
#         break
# if len(res) == 1:
#     print(res[0])
# else:
#     print(-1)
#


# def main():
#     f = open('input.txt', 'r')
#     res = []
#     ind = 1
#     s = f.read(1)
#
#     c = {"{": 0, "}": 0}
#     simb_bef = ""
#     f_l = -1
#     f_r = -1
#     l_l = [False, -1]
#     fi_r = [False, -1]
#     while s != '\n':
#         if s == "{":
#             if c["{"] - c["}"] == 0:
#                 f_l = ind
#             c["{"] += 1
#         elif s == "}":
#             if f_l == f_r == -1:
#                 l_l[1] = ind
#                 l_l[0] = True
#             if f_r == -1:
#                 f_r = ind
#             c["}"] += 1
#         ind += 1
#         simb_bef = s
#         s = f.read(1)
#     if simb_bef == "{":
#         fi_r[1] = ind-1
#         fi_r[0] = True
#     a = c["{"] - c["}"]
#     if abs(a) == 1:
#         if a > 0:
#             if fi_r[0]:
#                 res.append(fi_r[1])
#             else:
#                 res.append(f_l)
#         else:
#             if l_l[0]:
#                 res.append(l_l[1])
#             else:
#                 res.append(f_r)
#
#     if len(res) != 1:
#         print(-1)
#     else:
#         print(res[0])
#
#
# main()

f = open('input.txt', 'r')
s = f.readline()
n = len(s)
lst = list()
for i in range(n):
    if not s[i] in "{}":
        continue
    if s[i] == '}' and len(lst) > 0 and lst[-1][0] == '{':
        lst.pop()
    else:
        lst.append([s[i], i + 1])
print(lst)
if len(lst) == 2 and lst[0][0] == lst[1][0]:
    if lst[0][0] == '{':
        print((n - lst[1][1]) // 2 + 1)
    else:
        print(lst[0][1] // 2 + 1)
else:
    print(-1)