#268. Missing Number
class Solution(object):
    def missingNumber(self,nums):
        n=len(nums)#this line upper bound because if the missing this line then missing the last value
        for i in range(0,n+1):#range start by 0 to n+1
            if i not in nums:#check aray all numbers and find missing the value
                return i#return missing the value from i


nums=[0,2,3,]
obj=Solution()
array=obj.missingNumber(nums)
print(array)