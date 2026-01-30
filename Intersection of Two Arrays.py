class Solution(object):
    def intersection(self,nums1,nums2):#this function will find intersection between nums1 and nums2
        set1=set(nums1)#for unique value
        result=set()#empty

        for i in nums2:#check all elements nums2
            if i in set1:#check set1 and i value same or not because set1 unique element
                result.add(i)
        return list(result)

nums1=[1,2,2,3]
nums2=[2,2]
obj=Solution()
array=obj.intersection(nums1,nums2)
print(array)