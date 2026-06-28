class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0
        arr.sort()
        n = len(arr)
        ans = 1
        cur_min = float('inf')
        for r in range(1, n + 1):
            val = arr[n - r] + r - 1
            cur_min = min(cur_min, val)
            if cur_min >= r:
                ans = r
        return ans