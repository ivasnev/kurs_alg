# TOP 99,74(127 ms) 99,77(152 mb)

class Solution:
    def solve(self, board):
        m, n = len(board), len(board[0])
        stack = [ij for k in range(m) for ij in ((k, 0), (k, n - 1))]
        stack += [ij for k in range(n) for ij in ((0, k), (m - 1, k))]
        while stack:
            i, j = stack.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = '.'
                stack += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)
        board[:] = [['XO'[c == '.'] for c in row] for row in board]
