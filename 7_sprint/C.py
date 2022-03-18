from queue import PriorityQueue


def main():
    m = int(input())
    n = int(input())
    heaps = []
    for i in range(n):
        heaps.append(list(map(int, input().split())))
    heaps.sort(key=lambda x: x[0])
    cost = 0
    tmp_m = 0
    for i in range(n):
        if tmp_m != m:
            item = heaps.pop()
            if tmp_m + item[1] < m:
                a = item[1]
            else:
                a = m - tmp_m
            cost += (item[0]) * a
            tmp_m += a
        else:
            break
    print(cost)


if __name__ == '__main__':
    main()
