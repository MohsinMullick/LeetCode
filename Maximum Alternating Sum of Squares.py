class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        odd = 0
        even = 0

        for x in nums:
            new_odd = max(odd, even + x)
            new_even = max(even, odd - x)
            odd, even = new_odd, new_even

        return odd