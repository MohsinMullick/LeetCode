class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        freq = [0] * (n + 1)
        common = 0
        result = []
        for i in range(n):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common += 1
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common += 1
            result.append(common)
        return result