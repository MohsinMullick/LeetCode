from itertools import permutations

class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        valid = set()
        for perm in permutations(digits, 3):
            if perm[0] == 0:
                continue
            if perm[2] % 2 != 0:
                continue
            valid.add(perm[0] * 100 + perm[1] * 10 + perm[2])
        return len(valid)