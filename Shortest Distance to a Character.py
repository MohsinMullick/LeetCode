class Solution(object):
    def shortestToChar(self, s, c):
        n = len(s)
        result = [0] * n
        prev = float('-inf')
        # Left to Right
        for i in range(n):
            if s[i] == c:
                prev = i
            result[i] = i - prev
        prev = float('inf')
        # Right to Left
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            result[i] = min(result[i], prev - i)
        return result