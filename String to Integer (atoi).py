class Solution(object):
    def myAtoi(self, s):
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        i, n = 0, len(s)

        while i < n and s[i] == ' ':
            i += 1

        sign = 1
        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        res = 0
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            if sign * res >= INT_MAX:
                return INT_MAX
            if sign * res <= INT_MIN:
                return INT_MIN
            i += 1

        return sign * res