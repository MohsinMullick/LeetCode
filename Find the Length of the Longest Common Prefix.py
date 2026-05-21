class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        prefix_set = set()

        # Store all prefixes of arr1 numbers
        for x in arr1:
            while x > 0:
                prefix_set.add(x)
                x //= 10

        best = 0

        # Check all prefixes of arr2 numbers against the set
        for y in arr2:
            while y > 0:
                if y in prefix_set:
                    best = max(best, len(str(y)))
                    break          # shorter prefixes of y can't beat this
                y //= 10

        return best