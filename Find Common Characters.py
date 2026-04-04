class Solution(object):
    def commonChars(self, words):
        from collections import Counter
        # Step 1: first word er count
        common = Counter(words[0])
        # Step 2: baki word gula diye update
        for word in words[1:]:
            common &= Counter(word)
        # Step 3: result build
        result = []
        for char in common:
            result.extend([char] * common[char])
        return result