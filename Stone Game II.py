class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        # suffix_sum[i] = sum of piles[i:]
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        memo = {}

        def dp(i, M):
            if i >= n:
                return 0
            if (n - i) <= 2 * M:
                return suffix_sum[i]
            if (i, M) in memo:
                return memo[(i, M)]

            best = 0
            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break
                cur = suffix_sum[i] - dp(i + X, max(M, X))
                if cur > best:
                    best = cur

            memo[(i, M)] = best
            return best

        return dp(0, 1)