class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        res = 0
        # Check from the left: compare colors[0] with every house from the right
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                res = max(res, i)
                break
        # Check from the right: compare colors[n-1] with every house from the left
        for i in range(n):
            if colors[i] != colors[n - 1]:
                res = max(res, n - 1 - i)
                break
        return res