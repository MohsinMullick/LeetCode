class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = '1' + s + '1'
        groups = []
        i, m = 0, len(t)
        while i < m:
            j = i
            while j < m and t[j] == t[i]:
                j += 1
            groups.append((t[i], j - i))
            i = j

        total_ones = s.count('1')
        max_gain = 0

        for idx in range(1, len(groups) - 1):
            char, length = groups[idx]
            if char == '1':
                left_char, left_len = groups[idx - 1]
                right_char, right_len = groups[idx + 1]
                # these are guaranteed to be '0' groups since groups alternate
                max_gain = max(max_gain, left_len + right_len)

        return total_ones + max_gain