x = int(input())
n = 0
while 4**n < x:
    n += 1
if 4**n == x:
    print("True")
else:
    print("False")