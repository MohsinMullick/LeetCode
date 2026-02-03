class Solution(object):
    def findMaxConsecutiveOnes(self,nums):
        count=0#assume count value 0
        maxcount=0#maxcount value 0
        for num in nums:#use for traverse
            if num==1:#fixed assume 1
                count+=1#if num==1 then increase 1
                maxcount=max(maxcount,count)#find the max count
            else:
                count=0
        return maxcount#retrun print value
#-------Main part------
nums=[1,1,0,0,1,1,1,1,0,1]
obj=Solution()
array=obj.findMaxConsecutiveOnes(nums)
print(array)