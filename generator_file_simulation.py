states = [[-1, -2, -3, -4, -5, -6, -7, -8], [4, 7], [-4, 5, -7], [2, 3, 4, 6, 7, 8], [-3, -4, -8],
          [1, -2, -5, -6, -7, 8], [3, 6], [2, -3, -8], [-1, -2, 4, 5, -6, 8], [1, 2, 3, -4, -5, -8], [6, 8], [5],
          [-1, -3, 4, -5], [1, 3, 5, -6, 7], [-1, -2, -3, -4, -5, 6, -7, -8], [2, 3, 4, 5, -6, 7, 8], [-5], [5, -7, -8]]


def generate():
    state = [0 for i in range(24)]
    counter = 0
    print("1|1|2|2|3|3|4|4|5|5|6|6|7|7|8|8|1|2|3|4|5|6|7|8")
    print(
        "0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|# Init 1/3/5/7/9/11/13/15-концевик верх 2/4/6/8/10/12/14/16-концевик вниз 5/6{0-sigUP 1-sigDown}")
    for s in states:
        for i in s:
            if i > 0:
                state[15 + abs(i)] = 1
            else:
                state[15 + abs(i)] = 0
        print("|".join(map(str, state)) + "|# (" + " ".join(map(str, s)) + ") Start")
        for i in s:
            index = (abs(i) - 1) * 2
            if i > 0:
                state[index], state[index + 1] = 1, 0
            else:
                state[index], state[index + 1] = 0, 1
        print("|".join(map(str, state)) + "|# (" + " ".join(map(str, s)) + ") Finish")
        print("|".join(map(str, state)) + "|# (" + " ".join(map(str, s)) + ") Stay in state_", counter, sep="")
        counter += 1


generate()
