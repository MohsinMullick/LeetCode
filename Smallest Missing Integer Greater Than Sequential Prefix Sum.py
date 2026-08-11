class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find length of the longest prefix that forms a consecutive sequence
        n = len(nums)
        prefix_len = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                prefix_len += 1
            else:
                break

        # Sum of that consecutive prefix
        target = sum(nums[:prefix_len])

        # Find smallest integer >= target not present in nums
        num_set = set(nums)
        while target in num_set:
            target += 1

        return target