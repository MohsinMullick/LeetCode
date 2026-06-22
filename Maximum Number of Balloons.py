from collections import Counter


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        count = Counter(text)
        b = count.get('b', 0)
        a = count.get('a', 0)
        l = count.get('l', 0)
        o = count.get('o', 0)
        n = count.get('n', 0)

        # 'balloon' requires: b:1, a:1, l:2, o:2, n:1
        return min(b, a, l // 2, o // 2, n)