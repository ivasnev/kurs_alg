from functools import reduce

def hesh_t(line):
    line = list(line)
    a = 1000
    m = 123987123
    n = len(line)
    if n != 0:
        line[0] = ord(line[0])

        def gorner(s0, s1):
            return (s0 * a + ord(s1))%m

        h = (reduce(gorner, line))%m
        print(h)
        return(h)
    else:
        print(0)
        return 0

a = 1000
m = 123987123
c = hesh_t("ezhgeljkablzwnvuwqvqa")
b = hesh_t("gbpdcvkumyfxillgnqrwa")
#
# print(47021983, (47021983+m))

# for a in range(97, 123):
#     for b in range(97, 123):
#         for c in range(97, 123):
#             for d in range(97, 123):
#                 for e in range(97, 123):
#                     # print((a * 1000 ** 4 + b * 1000 ** 3 + c * 1000**2 + d * 1000 + e) % m)
#                     if (a * 1000 ** 4 + b * 1000 ** 3 + c * 1000**2 + d * 1000 + e) % m == 47021983:
#                         print(a, b, c, d, e)

# for n in range(3, 10):
#     line = ["a" for i in range(n)]
#     line[0] = ord(line[0])
#
#
#     def gorner(s0, s1):
#         return (s0 * a + ord(s1))
#
#
#     h_1 = (reduce(gorner, line))
#     line = ["z" for i in range(n)]
#     line[0] = ord(line[0])
#
#
#     def gorner(s0, s1):
#         return (s0 * a + ord(s1))
#
#
#     h_2 = (reduce(gorner, line))
#     print(n,"|", h_1, h_2, "|", h_1 // m, h_2 // m, )
