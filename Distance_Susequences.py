class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        if n > m:
            return 0

        # dp[j] represents dp[i][j] for current i, rolled into 1D array
        dp = [0] * (n + 1)
        dp[0] = 1  # empty t is always formed exactly 1 way

        for i in range(1, m + 1):
            # iterate j backwards so dp[j-1] still refers to previous row (i-1)
            for j in range(min(i, n), 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]