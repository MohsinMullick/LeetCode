class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10 ** 9 + 7
        n = len(s)

        # pow10[i] = 10^i mod MOD, i up to n
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = pow10[i - 1] * 10 % MOD

        # prefix sum of raw digit values (zeros contribute 0 anyway)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + int(s[i])

        # segment tree size = next power of two >= n
        size = 1
        while size < max(n, 1):
            size *= 2

        val = [0] * (2 * size)
        cnt = [0] * (2 * size)

        for i in range(n):
            d = int(s[i])
            if d != 0:
                val[size + i] = d
                cnt[size + i] = 1
            # else stays (0,0) which is identity

        for i in range(size - 1, 0, -1):
            lc, rc = 2 * i, 2 * i + 1
            cnt[i] = cnt[lc] + cnt[rc]
            val[i] = (val[lc] * pow10[cnt[rc]] + val[rc]) % MOD

        def merge(a, b):
            av, ac = a
            bv, bc = b
            return ((av * pow10[bc] + bv) % MOD, ac + bc)

        def query(l, r):  # inclusive 0-indexed range
            l += size
            r += size + 1
            resl = (0, 0)
            resr = (0, 0)
            while l < r:
                if l & 1:
                    resl = merge(resl, (val[l], cnt[l]))
                    l += 1
                if r & 1:
                    r -= 1
                    resr = merge((val[r], cnt[r]), resr)
                l >>= 1
                r >>= 1
            return merge(resl, resr)

        ans = []
        for l, r in queries:
            x_val, _ = query(l, r)
            digit_sum = prefix[r + 1] - prefix[l]
            ans.append((x_val * digit_sum) % MOD)

        return ans