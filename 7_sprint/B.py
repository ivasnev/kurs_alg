def main():
    n = int(input())
    list_urok = []
    for i in range(n):
        a, b = map(float, input().split())
        list_urok.append([a, b])
    list_urok.sort(key=lambda x: (-x[1], -x[0]))
    print(list_urok)
    out = []
    time = 0
    counter = 0
    for i in range(n):
        item = list_urok.pop()
        if time <= item[0]:
            counter += 1
            time = item[1]
            out.append([item[0], time])
    print(counter)
    for i in out:
        print(" ".join(map(str, i)))


main()

