class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        def calc(a1, t1, a2, t2):
            # Earliest finish time of any ride in first group
            min_end = min(a + t for a, t in zip(a1, t1))
            # For each ride in second group, compute finish time after min_end
            return min(max(a, min_end) + t for a, t in zip(a2, t2))

        # Try land first then water
        x = calc(landStartTime, landDuration, waterStartTime, waterDuration)
        # Try water first then land
        y = calc(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(x, y)