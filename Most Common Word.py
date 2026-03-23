class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        import re
        from collections import Counter
        # Step 1: lowercase + remove punctuation
        words = re.findall(r'\w+', paragraph.lower())
        # Step 2: banned set
        banned_set = set(banned)
        # Step 3: filter + count
        count = Counter(w for w in words if w not in banned_set)
        # Step 4: return most common
        return count.most_common(1)[0][0]