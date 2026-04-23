from collections import defaultdict


class Solution(object):
    def distance(self, nums):
        pos = defaultdict(list)

        # Step 1: group indices
        for i, num in enumerate(nums):
            pos[num].append(i)

        res = [0] * len(nums)

        # Step 2: process each group
        for num in pos:
            arr = pos[num]
            n = len(arr)

            prefix = [0] * (n + 1)

            # prefix sum of indices
            for i in range(n):
                prefix[i + 1] = prefix[i] + arr[i]

            for i in range(n):
                idx = arr[i]

                # left side
                left = idx * i - prefix[i]

                # right side
                right = (prefix[n] - prefix[i + 1]) - idx * (n - i - 1)

                res[idx] = left + right

        return res