class Solution(object):
    def isAlienSorted(self, words, order):
        # Step 1: create order mapping
        order_map = {char: i for i, char in enumerate(order)}
        # Step 2: compare adjacent words
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            # Step 3: compare characters
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if order_map[w1[j]] > order_map[w2[j]]:
                        return False
                    break
            else:
                # Step 4: prefix case
                if len(w1) > len(w2):
                    return False

        return True