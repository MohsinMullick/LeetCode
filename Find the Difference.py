from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        count = Counter(t)
        for ch in s:
            count[ch] -= 1
            if count[ch] == 0:
                del count[ch]
        return list(count.keys())[0]