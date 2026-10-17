class Solution(object):
    def minSwaps(self, nums):
        n = len(nums)
        k = sum(nums)
        if k == 0 or k == n:
            return 0

        cur = sum(nums[:k])
        best = cur

        for i in range(1, n):
            cur += nums[(i + k - 1) % n] - nums[i - 1]
            if cur > best:
                best = cur

        return k - best