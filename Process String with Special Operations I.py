class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for c in s:
            if c.isalpha():
                result.append(c)
            elif c == "*" and result:
                result.pop()
            elif c == "#":
                # Use a copy to avoid infinite extension
                result.extend(result[:])
            elif c == "%":
                result.reverse()
        return "".join(result)