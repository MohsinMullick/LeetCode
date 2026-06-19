class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current = 0
        max_alt = 0
        for g in gain:
            current += g
            if current > max_alt:
                max_alt = current
        return max_alt