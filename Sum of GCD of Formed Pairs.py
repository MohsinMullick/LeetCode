class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        prefixGcd = []
        mx = 0
        for i in range(n):
            mx = max(mx, nums[i])
            prefixGcd.append(gcd(nums[i], mx))
        prefixGcd.sort()

        total = 0
        l, r = 0, n - 1
        while l < r:
            total += gcd(prefixGcd[l], prefixGcd[r])
            l += 1
            r -= 1
        return total