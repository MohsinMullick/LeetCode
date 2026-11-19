from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        w = len(words[0])
        n = len(words)
        need = Counter(words)
        res = []

        for off in range(w):
            left = off
            count = 0
            seen = {}
            for right in range(off, len(s) - w + 1, w):
                word = s[right:right + w]
                if word in need:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1
                    while seen[word] > need[word]:
                        lw = s[left:left + w]
                        seen[lw] -= 1
                        count -= 1
                        left += w
                    if count == n:
                        res.append(left)
                        lw = s[left:left + w]
                        seen[lw] -= 1
                        count -= 1
                        left += w
                else:
                    seen = {}
                    count = 0
                    left = right + w
        return res