n = int(input())
m = int(input())
array = []
for y in range(n):
    array.append(list(int(x) for x in input().split()))
y = int(input())
x = int(input())

neighbourhoods = []

if y + 1 < n:
    neighbourhoods.append(array[y + 1][x])
if y - 1 >= 0:
    neighbourhoods.append(array[y - 1][x])
if x + 1 < m:
    neighbourhoods.append(array[y][x + 1])
if x - 1 >= 0:
    neighbourhoods.append(array[y][x - 1])

neighbourhoods.sort()
for i in neighbourhoods:
    print(i, end=' ')

