class Solution(object):
    def moveZeroes(self, nums):
        pos = 0
        # Move non-zero elements forward
        for i in range(len(nums)):#length
            if nums[i] != 0:#non-zero cheeck
                nums[pos] = nums[i]
                pos += 1
        # Fill remaining positions with zero
        for i in range(pos, len(nums)):
            nums[i] = 0

nums=[0,1,2,3,0,4]
obj=Solution()
obj.moveZeroes(nums)
print(nums)
