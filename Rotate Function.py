class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)

        # Compute F(0)
        F = sum(i * nums[i] for i in range(n))
        max_val = F

        # Compute other F(k)
        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            max_val = max(max_val, F)

        return max_val