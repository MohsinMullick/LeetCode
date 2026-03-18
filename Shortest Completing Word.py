class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        from collections import Counter
        # Step 1: licensePlate theke letter count
        lp_count = Counter(c.lower() for c in licensePlate if c.isalpha())
        result = None
        # Step 2: check each word
        for word in words:
            w_count = Counter(word.lower())
            valid = True
            for c in lp_count:
                if w_count[c] < lp_count[c]:
                    valid = False
                    break
            # Step 3: update shortest word
            if valid:
                if result is None or len(word) < len(result):
                    result = word
        return result