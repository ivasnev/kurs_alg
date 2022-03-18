

def main():
    n, m = map(int, input().split())
    map_of_flowers = []
    for _ in range(n):
        map_of_flowers.append([-float("inf")] + [int(x) for x in input()])
    map_of_flowers.append([-float("inf") for _ in range(m + 1)])
    for y in range(n - 1, -1, -1):
        for x in range(1, m + 1):
            if not (x == 1 and y == n - 1):
                map_of_flowers[y][x] = max(map_of_flowers[y + 1][x], map_of_flowers[y][x - 1]) + map_of_flowers[y][x]
    print(map_of_flowers[0][m])
    path = ""
    x = m
    y = 0
    while not(x == 1 and y == n - 1):
        if map_of_flowers[y + 1][x] > map_of_flowers[y][x - 1]:
            y += 1
            path += "U"
        else:
            x -= 1
            path += "R"
    print(path[::-1])



if __name__ == '__main__':
    main()
