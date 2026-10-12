class Solution(object):
    def maxSum(self, nums, k):
        n = len(nums)
        if k <= 0 or k > n:
            return 0

        window = sum(nums[:k])
        best = window

        for i in range(k, n):
            window += nums[i] - nums[i - k]
            best = max(best, window)

        return best