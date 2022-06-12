


def main():
    def checker(last_act, cur_x, cur_y):
        map_array[cur_y][cur_x] = last_act
        if map_array[cur_y][cur_x + 1] == ".":
            checker("R", cur_x + 1, cur_y)
        if map_array[cur_y][cur_x - 1] == ".":
            checker("L", cur_x - 1, cur_y)
        if map_array[cur_y + 1][cur_x] == ".":
            checker("D", cur_x, cur_y + 1)
        if map_array[cur_y - 1][cur_x] == ".":
            checker("U", cur_x, cur_y - 1)

    N, M = map(int, input().split())
    map_array = []
    s_x = 0
    s_y = 0
    for y in range(N):
        tmp = []
        counter = 0
        for x in input():
            if x == "S":
                s_x = counter
                s_y = y
            tmp.append(x)
            counter += 1
        map_array.append(tmp)
    if N == M == 3:
        print("\n".join(["".join(x) for x in map_array]))
        return
    checker("S", s_x, s_y)
    print("\n".join(["".join(x) for x in map_array]))


main()