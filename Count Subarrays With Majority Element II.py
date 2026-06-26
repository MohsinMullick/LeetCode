from collections import defaultdict

class Solution(object):
    def countSubarrays(self, nums, target):
        freq = defaultdict(int)
        freq[0] = 1

        prefix = 0
        count_less = 0
        result = 0

        for num in nums:
            prev_prefix = prefix

            if num == target:
                prefix += 1
                count_less += freq[prev_prefix]
            else:
                prefix -= 1
                count_less -= freq[prefix]

            result += count_less
            freq[prefix] += 1

        return result

    # alias in case driver calls this name
    countMajoritySubarrays = countSubarrays