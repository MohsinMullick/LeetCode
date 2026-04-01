class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        low, high = 0, len(s)
        result = []
        for ch in s:
            if ch == 'I':
                result.append(low)
                low += 1
            else:  # 'D'
                result.append(high)
                high -= 1
        result.append(low)  # last remaining number
        return result