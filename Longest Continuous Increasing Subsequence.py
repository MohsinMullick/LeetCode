class Solution(object):
    def findLengthOfLCIS(self,nums):
        if not nums:#if array list empty then false but not nums true because bool(nums)->false
            return 0
        max_length=current_length=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                current_length+=1
            else:
                current_length=1
            max_length=max(max_length,current_length)
        return max_length
nums=[1,2,3,4]
obj=Solution()
array=obj.findLengthOfLCIS(nums)
print(array)