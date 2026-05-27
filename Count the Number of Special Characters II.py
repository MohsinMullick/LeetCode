class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        first_upper = [n] * 26
        last_lower = [-1] * 26

        for i, c in enumerate(word):
            if 'a' <= c <= 'z':
                idx = ord(c) - ord('a')
                last_lower[idx] = i
            elif 'A' <= c <= 'Z':
                idx = ord(c) - ord('A')
                first_upper[idx] = min(first_upper[idx], i)

        count = 0
        for i in range(26):
            if last_lower[i] != -1 and first_upper[i] < n:
                if last_lower[i] < first_upper[i]:
                    count += 1
        return count