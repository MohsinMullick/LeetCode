class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:#trsverse
            if num in seen:#check
                return True
            seen.add(num)#seen numbers add
        return False

#-----Main-----
nums=[1,2,3,1]
obj=Solution()
array=obj.containsDuplicate(nums)
print(array)

