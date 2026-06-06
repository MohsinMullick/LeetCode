class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, r = 0, sum(nums)
        ans = []
        for x in nums:
            r -= x
            ans.append(abs(l - r))
            l += x
        return ans