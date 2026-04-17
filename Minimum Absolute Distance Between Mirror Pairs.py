class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def reverse_num(x):
            return int(str(x)[::-1])

        from collections import defaultdict

        # reverse(nums[i]) -> [i, ...] store করো
        rev_of_val = defaultdict(list)
        min_dist = float('inf')

        for j, x in enumerate(nums):
            # x == reverse(nums[i]) এমন i আছে কিনা দেখো
            if x in rev_of_val:
                closest_i = rev_of_val[x][-1]  # সবচেয়ে কাছের
                min_dist = min(min_dist, j - closest_i)

            # reverse(x) কে map এ রাখো, key = reverse(x), value = j
            rev_x = reverse_num(x)
            rev_of_val[rev_x].append(j)

        return min_dist if min_dist != float('inf') else -1
sol = Solution()

print(sol.minMirrorPairDistance([12, 21, 45, 33, 54]))  # Output: 1
print(sol.minMirrorPairDistance([120, 21]))              # Output: 1
print(sol.minMirrorPairDistance([21, 120]))              # Output: -1