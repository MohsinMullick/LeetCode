class Solution(object):
    def minOperations(self, s):
        n = len(s)
        if s == "".join(sorted(s)):
            return 0
        if n == 2:
            return -1
        mn, mx = min(s), max(s)
        if s[0] == mn or s[-1] == mx:
            return 1
        if mx in s[1:] or mn in s[:-1]:
            return 2
        return 3