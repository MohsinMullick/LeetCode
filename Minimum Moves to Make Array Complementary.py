class Solution(object):
    def minMoves(self, nums, limit):
        n = len(nums)
        # diff array for targets 2..2*limit (size 2*limit+2)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            lo = min(a, b)
            hi = max(a, b)

            # Default: 2 moves needed for all targets [2, 2*limit]
            # Range [lo+1, hi+limit]: only 1 move needed (-1 from base 2)
            # Exactly [a+b]: 0 moves needed (-1 more)

            # Apply -1 for range [lo+1, hi+limit]
            diff[lo + 1] -= 1
            diff[hi + limit + 1] += 1

            # Apply -1 for exact target a+b
            diff[a + b] -= 1
            diff[a + b + 1] += 1

        # Sweep: start with base cost n//2 pairs * 2 moves each
        # but we encoded +2 per pair implicitly; reconstruct:
        result = float('inf')
        base = n  # n//2 pairs * 2
        current = base

        for t in range(2, 2 * limit + 1):
            current += diff[t]
            result = min(result, current)

        return result