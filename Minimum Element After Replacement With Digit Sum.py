class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def digit_sum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        if not nums:
            return 0  # or handle empty case as per constraints

        min_val = float('inf')
        for num in nums:
            current_sum = digit_sum(num)
            if current_sum < min_val:
                min_val = current_sum

        return min_val