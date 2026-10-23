class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -1 
        for i, x in enumerate(nums):
            if x != i:
                ans &= x
        return 0 if ans == -1 else ans