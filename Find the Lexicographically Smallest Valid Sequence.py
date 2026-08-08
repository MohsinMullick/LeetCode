class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n, m = len(word1), len(word2)
        if m > n:
            return []

        # suf[j] = max starting index p in word1 such that word2[j:] is still
        # an exact subsequence of word1[p:] (computed by matching from the right)
        suf = [-1] * (m + 1)
        suf[m] = n  # empty suffix always matches, sentinel
        ptr = n - 1
        for j in range(m - 1, -1, -1):
            while ptr >= 0 and word1[ptr] != word2[j]:
                ptr -= 1
            if ptr < 0:
                suf[j] = -1
            else:
                suf[j] = ptr
                ptr -= 1

        res = []
        i = 0
        j = 0
        used_mismatch = False

        while j < m:
            if i >= n:
                return []
            if word1[i] == word2[j]:
                res.append(i)
                i += 1
                j += 1
            else:
                if (not used_mismatch) and i + 1 <= suf[j + 1]:
                    res.append(i)
                    used_mismatch = True
                    i += 1
                    j += 1
                else:
                    i += 1

        return res if j == m else []