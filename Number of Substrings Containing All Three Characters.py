class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = [-1, -1, -1]
        ans = 0
        for i in range(len(s)):
            last[ord(s[i]) - ord('a')] = i
            if min(last) >= 0:
                ans += min(last) + 1
        return ans