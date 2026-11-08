class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            best = max(best, w * h)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best