class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # Min must be in right portion (after mid)
                # e.g. [4,5,6,7,*0*,1,4] → mid=6, right=4 → go right
                left = mid + 1

            elif nums[mid] < nums[right]:
                # Mid could be the minimum, so keep it
                # e.g. [4,5,*1*,2,3] → mid=1, right=3 → go left incl. mid
                right = mid

            else:
                # nums[mid] == nums[right]: ambiguous due to duplicates
                # e.g. [1,*1*,1,0,1] → can't tell which side, shrink right
                right -= 1

        return nums[left]