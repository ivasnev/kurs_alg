def check_win(moves):
    def win(player_moves, last_move):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            for i in range(1, 5):
                if (last_move[0] + dx * i, last_move[1] + dy * i) in player_moves:
                    count += 1
                else:
                    break
            for i in range(1, 5):
                if (last_move[0] - dx * i, last_move[1] - dy * i) in player_moves:
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False

    player_moves = [{}, {}]
    winner = None
    for i, (r, c) in enumerate(moves):
        current_player = i % 2
        player_moves[current_player][(r, c)] = True
        if win(player_moves[current_player], (r, c)):
            winner = "First" if current_player == 0 else "Second"
            break
    if winner:
        if i + 1 < len(moves):
            return "Inattention"
        else:
            return winner
    else:
        return "Draw"


n = int(input().strip())
moves = [tuple(map(int, input().split())) for _ in range(n)]
print(check_win(moves))