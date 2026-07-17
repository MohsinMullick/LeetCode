import bisect

class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        maxVal = max(nums)
        freq = [0] * (maxVal + 1)
        for x in nums:
            freq[x] += 1

        # cnt[v] = number of elements in nums divisible by v
        cnt = [0] * (maxVal + 1)
        for v in range(1, maxVal + 1):
            for m in range(v, maxVal + 1, v):
                cnt[v] += freq[m]

        # pairs[v] = number of pairs (i<j) whose gcd is exactly v
        pairs = [0] * (maxVal + 1)
        for v in range(maxVal, 0, -1):
            c = cnt[v]
            total = c * (c - 1) // 2
            for m in range(2 * v, maxVal + 1, v):
                total -= pairs[m]
            pairs[v] = total

        # prefix[v] = total number of pairs with gcd <= v
        prefix = [0] * (maxVal + 1)
        for v in range(1, maxVal + 1):
            prefix[v] = prefix[v - 1] + pairs[v]

        answer = []
        for q in queries:
            v = bisect.bisect_right(prefix, q)
            answer.append(v)

        return answer