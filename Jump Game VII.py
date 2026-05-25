class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        if s[-1] == '1':
            return False
        dp = [False] * n
        dp[0] = True
        count = 0
        for i in range(minJump, n):
            count += 1 if dp[i - minJump] else 0
            if i - maxJump > 0:
                count -= 1 if dp[i - maxJump - 1] else 0
            if count > 0 and s[i] == '0':
                dp[i] = True
        return dp[-1]