class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        # dp[i] = current player ar sokoler moddhe best "score difference"
        # (current player's score - opponent's score) index i theke start korle
        dp = [0] * (n + 1)

        # peeche theke build korbo, karon dp[i] depend kore dp[i+1], dp[i+2], dp[i+3] er upor
        for i in range(n - 1, -1, -1):
            best = float('-inf')
            take = 0
            # 1, 2, ba 3 ta stone nite pare
            for k in range(1, 4):
                if i + k > n:
                    break
                take += stoneValue[i + k - 1]
                # take korlam 'take' value, baki ta opponent optimal khelbe -> dp[i+k]
                # tai amar net gain = take - dp[i+k]
                best = max(best, take - dp[i + k])
            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"