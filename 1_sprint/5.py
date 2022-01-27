n = int(input())
array = input().split()
max = len(sorted(array, key=len)[-1])
for i in array:
    if len(i) == max:
        print(i)
        print(max)
        break

