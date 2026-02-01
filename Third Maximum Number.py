class Solution(object):
    def thirdMax(self,nums):
        set1=set(nums)#remove duplicate
        set1=list(set1)#convert to list
        set1.sort(reverse=True)#sort for descending order
        if len(set1)>=3:
            return set1[2]
        else:
            return set1[0]

nums=[1,2,3,4,5,5]
obj=Solution()
array=obj.thirdMax(nums)
print(array)