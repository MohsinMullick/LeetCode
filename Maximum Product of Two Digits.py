class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = sorted(int(d) for d in str(n))
        return digits[-1] * digits[-2]