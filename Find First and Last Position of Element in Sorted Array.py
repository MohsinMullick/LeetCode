class Solution(object):
    def searchRange(self, nums, target):
        def find(left_most):
            lo, hi = 0, len(nums) - 1
            ans = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    ans = mid
                    if left_most:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return ans

        first = find(True)
        if first == -1:
            return [-1, -1]
        return [first, find(False)]