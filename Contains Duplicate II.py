class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        for i in range(len(nums)):#traverse
            if nums[i] in seen:#check condition
                if i - seen[nums[i]] <= k:#condition check
                    return True
            seen[nums[i]] = i
        return False
nums=[1,2,3,1]
k=3
obj=Solution()
array=obj.containsNearbyDuplicate(nums,k)
print(array)