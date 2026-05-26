class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        lower_mask = 0
        upper_mask = 0

        for c in word:
            if c.islower():
                lower_mask |= (1 << (ord(c) - ord('a')))
            else:
                upper_mask |= (1 << (ord(c.lower()) - ord('a')))

        # Count bits that are set in both masks
        common = lower_mask & upper_mask
        count = 0
        while common:
            count += common & 1
            common >>= 1

        return count