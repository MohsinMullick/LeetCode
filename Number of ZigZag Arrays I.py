class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        k = r - l + 1
        if n == 1:
            return k % MOD
        # Remap to 0..k-1
        prefix = [1] * k
        for i in range(1, k):
            prefix[i] = (prefix[i] + prefix[i - 1]) % MOD

        zig = True  # True for next should be greater (up)
        for _ in range(1, n - 1):
            if zig:
                # Next is greater: update prefix[j] += sum from j+1 to end
                for j in range(k - 2, -1, -1):
                    prefix[j] = (prefix[j] + prefix[j + 1]) % MOD
            else:
                # Next is smaller: update prefix[j] += sum from 0 to j-1
                for j in range(1, k):
                    prefix[j] = (prefix[j] + prefix[j - 1]) % MOD
            zig = not zig

        total = sum(prefix) % MOD
        total = (total * 2) % MOD
        return total