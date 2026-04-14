class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()
        n = len(robot)
        m = len(factory)
        # dp[i] = min distance to fix first i robots
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for pos, cap in factory:
            new_dp = dp[:]
            for i in range(n):
                dist = 0
                for k in range(1, cap + 1):
                    if i + k > n:
                        break
                    dist += abs(robot[i + k - 1] - pos)
                    new_dp[i + k] = min(new_dp[i + k], dp[i] + dist)
            dp = new_dp
        return dp[n]