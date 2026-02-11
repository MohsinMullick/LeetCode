class Solution(object):
    def findErrorNums(self,nums):
        n=len(nums)
        fre=[0]*(n+1)
        for num in nums:
            fre[num]+=1
            duplicate=missing=-1
        for i in range(1,n+1):
            if fre[i]==2:
                duplicate=i
            elif fre[i]==0:
                missing=i
        return (duplicate,missing)
nums=[1,2,2,4]
obj=Solution()
array=obj.findErrorNums(nums)
print(array)
