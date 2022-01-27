import math

def eratosthenes_effective(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(num * num, n + 1, num):
                numbers[j] = False
    return numbers

x = int(input())
ez_num = eratosthenes_effective(int(math.sqrt(x)))
fin_num = []
counter = 0
tmp_x = x
while counter < len(ez_num) and not(ez_num[counter]):
    counter += 1
while counter < len(ez_num) and ez_num[counter] < tmp_x:
    if tmp_x % ez_num[counter] == 0:
        fin_num.append(ez_num[counter])
        tmp_x = int(tmp_x / ez_num[counter])
    else:
        counter += 1
        while counter < len(ez_num) and not (ez_num[counter]):
            counter += 1
fin_num.append(tmp_x)
for i in fin_num:
    print(i,end=' ')
