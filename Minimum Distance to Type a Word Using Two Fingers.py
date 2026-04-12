class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        def dist(a, b):
            if a == 26:
                return 0
            r1, c1 = divmod(a, 6)
            r2, c2 = divmod(b, 6)
            return abs(r1 - r2) + abs(c1 - c2)

        dp = [float('inf')] * 27
        dp[26] = 0

        for i in range(len(word) - 1):
            cur = ord(word[i])     - ord('A')
            nxt = ord(word[i + 1]) - ord('A')
            new_dp = [float('inf')] * 27
            for other in range(27):
                if dp[other] == float('inf'):
                    continue
                cost = dp[other]
                # Move current finger to next
                new_dp[other] = min(new_dp[other], cost + dist(cur, nxt))
                # Move other finger to next
                new_dp[cur] = min(new_dp[cur], cost + dist(other, nxt))
            dp = new_dp
        return min(dp)