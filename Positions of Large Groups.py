class Solution(object):
    def largeGroupPositions(self, s):
        result = []
        start = 0
        for i in range(1, len(s)):
            if s[i] != s[start]:
                if i - start >= 3:
                    result.append([start, i - 1])
                start = i
        # last group check
        if len(s) - start >= 3:
            result.append([start, len(s) - 1])
        return result