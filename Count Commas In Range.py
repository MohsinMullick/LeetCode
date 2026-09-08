class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        d = 1
        low, high = 1, 9
        while low <= n:
            cur_high = min(high, n)
            count = cur_high - low + 1
            commas = (d - 1) // 3
            total += count * commas
            d += 1
            low = high + 1
            high = high * 10 + 9
        return total