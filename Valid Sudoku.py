class Solution(object):
    def isValidSudoku(self, board):
        seen = set()
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == '.':
                    continue
                keys = [(v, 'row', r), (v, 'col', c), (v, 'box', r // 3, c // 3)]
                for k in keys:
                    if k in seen:
                        return False
                    seen.add(k)
        return True