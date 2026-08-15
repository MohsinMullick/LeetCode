class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_xor = 0
        for x in nums:
            total_xor ^= x

        n = len(nums)

        if total_xor != 0:
            return n

        # total XOR is 0: dropping any single non-zero element
        # leaves XOR equal to that element (non-zero)
        if any(x != 0 for x in nums):
            return n - 1

        # all elements are zero -> every subsequence XORs to 0
        return 0