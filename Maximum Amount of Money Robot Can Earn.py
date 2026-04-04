class Solution(object):
    def maximumAmount(self, coins):
        m, n = len(coins), len(coins[0])
        # dp[i][j][k] → max money at (i,j) with k skips used
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        # start
        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0:
            dp[0][0][1] = 0  # skip
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if dp[i][j][k] == -float('inf'):
                        continue

                    for di, dj in [(0, 1), (1, 0)]:
                        ni, nj = i + di, j + dj
                        if ni >= m or nj >= n:
                            continue
                        val = coins[ni][nj]
                        # take value
                        dp[ni][nj][k] = max(dp[ni][nj][k],
                                            dp[i][j][k] + val)
                        # skip if negative
                        if val < 0 and k < 2:
                            dp[ni][nj][k + 1] = max(dp[ni][nj][k + 1],
                                                    dp[i][j][k])
        return max(dp[m - 1][n - 1])