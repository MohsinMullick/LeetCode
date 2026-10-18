class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(5000)
        MOD = 10**9 + 7
        n = len(nums)

        comb = [[1] * (i + 1) for i in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, i):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        def ways(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            return (comb[len(left) + len(right)][len(left)]
                    * ways(left) % MOD
                    * ways(right)) % MOD

        return (ways(nums) - 1) % MOD