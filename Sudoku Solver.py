class Solution(object):
    def solveSudoku(self, board):
        row = [0] * 9
        col = [0] * 9
        box = [0] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    d = int(board[i][j]) - 1
                    row[i] |= 1 << d
                    col[j] |= 1 << d
                    box[i // 3 * 3 + j // 3] |= 1 << d

        def dfs():
            bi = bj = -1
            best = 10
            bm = 0
            for i in range(9):
                for j in range(9):
                    if board[i][j] != '.':
                        continue
                    m = ~(row[i] | col[j] | box[i // 3 * 3 + j // 3]) & 511
                    c = bin(m).count('1')
                    if c < best:
                        best, bi, bj, bm = c, i, j, m
            if bi == -1:
                return True
            if best == 0:
                return False

            k = bi // 3 * 3 + bj // 3
            for d in range(9):
                if not (bm >> d & 1):
                    continue
                board[bi][bj] = str(d + 1)
                row[bi] |= 1 << d
                col[bj] |= 1 << d
                box[k] |= 1 << d
                if dfs():
                    return True
                row[bi] &= ~(1 << d)
                col[bj] &= ~(1 << d)
                box[k] &= ~(1 << d)
                board[bi][bj] = '.'
            return False

        dfs()