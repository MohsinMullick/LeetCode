class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        M = max(nums)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Precompute gcd(i, j) for all values 1..M
        gcd_table = [[0] * (M + 1) for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, M + 1):
                gcd_table[i][j] = gcd(i, j)

        # dp[g1][g2] = number of ways to split the processed prefix into
        # (seq1, seq2, unused) such that seq1's gcd is g1 (0 = empty)
        # and seq2's gcd is g2 (0 = empty)
        dp = [[0] * (M + 1) for _ in range(M + 1)]
        dp[0][0] = 1

        for num in nums:
            new_dp = [row[:] for row in dp]  # case: num goes to neither
            for g1 in range(M + 1):
                row = dp[g1]
                for g2 in range(M + 1):
                    c = row[g2]
                    if c == 0:
                        continue
                    # put num into seq1
                    ng1 = gcd_table[g1][num] if g1 != 0 else num
                    new_dp[ng1][g2] = (new_dp[ng1][g2] + c) % MOD
                    # put num into seq2
                    ng2 = gcd_table[g2][num] if g2 != 0 else num
                    new_dp[g1][ng2] = (new_dp[g1][ng2] + c) % MOD
            dp = new_dp

        ans = 0
        for g in range(1, M + 1):
            ans = (ans + dp[g][g]) % MOD
        return ans