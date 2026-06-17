class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # First pass: compute final length
        length = 0
        for c in s:
            if c == '*':
                length = max(0, length - 1)
            elif c == '#':
                length <<= 1  # length *= 2
            elif c != '%':
                length += 1
        if k >= length:
            return '.'

        # Second pass: backward simulation to find the k-th char
        for c in reversed(s):
            if c == '*':
                length += 1
            elif c == '#':
                length >>= 1  # length //= 2
                if k >= length:
                    k -= length
            elif c == '%':
                k = length - 1 - k
            else:
                # letter
                length -= 1
                if k == length:
                    return c
        return '.'