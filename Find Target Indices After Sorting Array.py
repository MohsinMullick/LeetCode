class Solution(object):
    def targetIndices(self, nums, target):
        less = 0
        equal = 0
        for n in nums:
            if n < target:
                less += 1
            elif n == target:
                equal += 1
        return list(range(less, less + equal))