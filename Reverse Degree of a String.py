class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i, ch in enumerate(s):
            value = 26 - (ord(ch) - ord('a'))  # 'a' -> 26, 'b' -> 25, ..., 'z' -> 1
            total += value * (i + 1)
        return total