class Solution(object):
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2:
            return False
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False

        half = (m + n - 1) // 2
        mask = (1 << (half + 1)) - 1

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    prev = 1
                else:
                    prev = 0
                    if i: prev |= dp[i-1][j]
                    if j: prev |= dp[i][j-1]

                if grid[i][j] == '(':
                    dp[i][j] = (prev << 1) & mask
                else:
                    dp[i][j] = prev >> 1

        return dp[m-1][n-1] & 1 == 1