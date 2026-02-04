class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:#zero error control
            return 0
        total = 0
        n = len(timeSeries)
        for i in range(1, n):#traverse
            gap = timeSeries[i] - timeSeries[i-1]#
            total += min(gap, duration)
        total += duration  # last attack
        return total
# ---------- MAIN PART ----------
timeSeries = [1, 4]
duration = 2

obj = Solution()
result = obj.findPoisonedDuration(timeSeries, duration)
print(result)

