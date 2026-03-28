class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        from collections import Counter
        # Split words and count frequency
        count = Counter((s1 + " " + s2).split())
        # Filter words that appear exactly once
        return [word for word in count if count[word] == 1]