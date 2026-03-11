class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace('-', '').upper()
        result = ""
        while len(s) > k:
            result = "-" + s[-k:] + result
            s = s[:-k]
        return s + result