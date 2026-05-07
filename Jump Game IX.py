class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)

        # prefix maximum
        preMax = [0] * n
        preMax[0] = nums[0]

        for i in range(1, n):
            preMax[i] = max(preMax[i - 1], nums[i])

        ans = [0] * n
        sufMin = float('inf')

        for i in range(n - 1, -1, -1):

            if preMax[i] > sufMin:
                ans[i] = ans[i + 1]
            else:
                ans[i] = preMax[i]

            sufMin = min(sufMin, nums[i])

        return ans