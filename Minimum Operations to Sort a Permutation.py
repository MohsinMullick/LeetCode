class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        p = nums.index(0)

        asc = all(nums[(p + i) % n] == i for i in range(n))
        desc = all(nums[(p + i) % n] == (n - i) % n for i in range(n))

        if not asc and not desc:
            return -1

        ans = float('inf')
        if asc:
            if p == 0:
                ans = 0
            else:
                ans = min(p, n - p + 2)
        if desc:
            q = n - 1 - p
            ans = min(ans, 1 + q, p + 2)
        return ans