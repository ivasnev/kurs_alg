# T = input()
# S = input()
# dif = 0
# for i in range(len(S)):
#     if T[i] != S[i]: dif += 1
# si = len(S)
# for left in range(1, len(T) - len(S)):
#     right = left + si
#     if T[left - 1] != S[0]:
#         dif -= 1
#     if T[right] != S[-1]:
#         dif += 1
#     if dif == 2:
#         print(left)
#         break
# else:
#     print(-1)
from collections import Counter

t = input('t = ')
s = input('s = ')
len_s = len(s)
t_lis = list(t)
c_s = Counter(s)
c_t = Counter(t_lis[:len_s])
c_res = dict()
summ = 0
for e in c_s:
    c_res[e] = [c_s[e], min(c_s[e], c_t[e])]
    summ += c_res[e][1]
for i in range(len(t) - len(s) + 1):
    if summ == len_s - 1:
        print(i)
        break
    if t[i] in c_res:
        if c_res[t[i]][1] > 0:
            c_res[t[i]][1] -= 1
            summ -= 1
    if i + len_s < len(t) and t[i + len_s] in c_res:
        if c_res[t[i + len_s]][1] < c_res[t[i + len_s]][0]:
            c_res[t[i + len_s]][1] += 1
            summ += 1
else:
    print(-1)
