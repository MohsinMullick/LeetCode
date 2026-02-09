class Solution(object):
    def maximumProduct(self,nums):
        nums.sort()
        a=nums[-1]*nums[-2]*nums[-3]#last 3 element multiply
        b=nums[0]*nums[1]*nums[-1]#first 2 and last one element multipy
        return max(a,b)#find the max number because im use max function thats python built in function
nums=[1,2,3]
obj=Solution()
array=obj.maximumProduct(nums)
print(array)