from functools import reduce
a = int(input())
m = int(input())
line = list(input())
n = len(line)

if n != 0:
    line[0] = ord(line[0])


    def gorner(s0,s1):
        return (s0*a + ord(s1))%m

    h = (reduce(gorner,line))%m
    print(h)
else:
    print(0)