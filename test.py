board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

if not any(board): print("sasa")

m, n = len(board), len(board[0])
save = [ij for k in range(m) for ij in ((k, 0), (k, n-1))]
save += [ij for k in range(n) for ij in ((0, k), (m-1, k))]
while save:
    i, j = save.pop()
    if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
        board[i][j] = 'S'
        save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)

board[:] = [['XO'[c == 'S'] for c in row] for row in board]