class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        # Sort tasks by (minimum - actual) descending
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        ans = 0
        cur = 0  # current remaining energy

        for actual, minimum in tasks:
            if cur < minimum:
                ans += minimum - cur
                cur = minimum
            cur -= actual

        return ans