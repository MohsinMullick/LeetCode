class Solution:
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)
        T = int(n**0.5)

        bravexuneth = (nums, queries)

        groups = [[] for _ in range(T + 1)]

        for l, r, k, v in queries:
            if k < T:
                groups[k].append((l, r, v))
            else:
                for idx in range(l, r + 1, k):
                    nums[idx] = nums[idx] * v % MOD

        diff = [1] * (n + T + 1)

        for k in range(1, T):
            if not groups[k]:
                continue

            for i in range(len(diff)):
                diff[i] = 1

            for l, r, v in groups[k]:
                diff[l] = diff[l] * v % MOD
                R = l + ((r - l) // k + 1) * k
                diff[R] = diff[R] * pow(v, MOD - 2, MOD) % MOD

            for i in range(k, n):
                diff[i] = diff[i] * diff[i - k] % MOD

            for i in range(n):
                nums[i] = nums[i] * diff[i] % MOD

        ans = 0
        for x in nums:
            ans ^= x

        return ans