"""
Given a sorted array of distinct integers and a target value,
 return the index if the target is found. If not,
return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""
class Solution(object):#create class
    def searchInsert(self,nums,target):#create function searchInsert, and nums=sorted array and target=insert or search value
        left=0#array index start zero
        right=len(nums)-1#array end index

        while left<=right:#condition check
            mid=(left+right)//2#mid point check integer division
            if nums[mid]==target:#mid and target value equal then return mid value
                return mid
            elif nums[mid]<target:#binary search condition
                left=mid+1
            else:
                right=mid-1#binary condition
        return left

#----------Main-------
nums=[1,3,5,6]#user  set the value
target=5#user target value 5
obj=Solution()#call the class
array=obj.searchInsert(nums,target)#call the function
print(f"Target Index: {array}")#print the position numbers 0,1,2,3,4,5,6 any 





