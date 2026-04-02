class Solution(object):
    def minDeletionSize(self, strs):
        rows = len(strs)
        cols = len(strs[0])
        count = 0
        for c in range(cols):
            for r in range(1, rows):
                if strs[r][c] < strs[r - 1][c]:
                    count += 1
                    break   
        return count