class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        prev = [set() for _ in range(n)]
        for r in range(m):
            cur = [None] * n
            for c in range(n):
                v = grid[r][c]
                if r == 0 and c == 0:
                    cur[c] = {v}
                    continue
                src = set()
                if r > 0:
                    src |= prev[c]
                if c > 0:
                    src |= cur[c - 1]
                cur[c] = {x ^ v for x in src}
            prev = cur
        return min(prev[n - 1])