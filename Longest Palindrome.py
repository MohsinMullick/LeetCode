class Solution(object):
    def longestPalindrome(self, s):
        char_count = {}
        # Count frequency
        for ch in s:
            char_count[ch] = char_count.get(ch, 0) + 1
        length = 0
        odd_found = False
        for count in char_count.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True
        if odd_found:
            length += 1
        return length