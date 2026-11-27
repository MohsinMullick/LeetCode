class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for _ in range(n - 1):
            res = []
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                res.append(str(j - i))
                res.append(s[i])
                i = j
            s = "".join(res)
        return s