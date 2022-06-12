n = int(input())
plane = [list(input()) for _ in range(n)]
left_window_empty = []
right_window_empty = []
left_aisle_empty = []
right_aisle_empty = []
for index_line in range(len(plane)):
    for index_seat in range(7):
        if index_seat == 3:
            continue
        item = plane[index_line][index_seat]
        if item == ".":
            if index_seat == 0:
                left_window_empty.append(index_line)
            elif index_seat == 2:
                left_aisle_empty.append(index_line)
            elif index_seat == 4:
                right_window_empty.append(index_line)
            elif index_seat == 6:
                right_aisle_empty.append(index_line)
m = int(input())
for _ in range(m):
    inp = input().split()
    window = False
    aisle = False
    left = False
    right = False
    quantity = int(inp[0])
    if inp[2] == "window":
        window = True
        if inp[1] == "right":
            right = True
            places = right_window_empty
            index = [6, 6 - quantity, -1]
        else:
            left = True
            places = left_window_empty
            index = [0, 0 + quantity]
    else:
        aisle = True
        if inp[1] == "right":
            right = True
            places = right_aisle_empty
            index = [4, 4 + quantity]
        else:
            left = True
            places = left_aisle_empty
            index = [2, 2 - quantity, -1]
    find_place = True
    for i in range(len(places)):
        i_l = places[i]
        flag = True
        for i_c in range(*index):
            if plane[i_l][i_c] == "#":
                flag = False
                break
        if flag:
            places.pop(i)
            print("Passengers can take seats: ", end="")
            letter = ["A", "B", "C", "_", "D", "E", "F"]
            t_p = []
            for i_c in range(*index):
                t_p.append(str(i_l + 1) + letter[i_c])
            t_p.sort()
            print(*t_p)
            for i_c in range(*index):
                plane[i_l][i_c] = "X"
            for line in plane:
                for s in line:
                    print(s, end="")
                print()
            for i_c in range(*index):
                plane[i_l][i_c] = "#"
            break
    else:
        find_place = False
    if not find_place:
        print("Cannot fulfill passengers requirements")
