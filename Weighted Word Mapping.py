class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        result = []
        for word in words:
            total = 0
            for char in word:
                total += weights[ord(char) - ord('a')]
            mod = total % 26
            # Map: 0 -> 'z', 1 -> 'y', ..., 25 -> 'a'
            mapped = chr(ord('z') - mod)
            result.append(mapped)
        return ''.join(result)