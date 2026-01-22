class Solution(object):
    def removeDuplicates(self, nums): # create function
        if not nums: # maintain for error because if nums create empty list then return 0
            return 0
        i = 0 # unique index track
        for j in range(1, len(nums)): # create loop for traverse and day that initial 1
            if nums[j] != nums[i]: # check element both are same or not,if not then check next index
                i += 1 # next index
                nums[i] = nums[j]
        return i + 1 # total unique count


# -------- main ----------
nums = [1, 1, 2]#declare input
obj = Solution()
k = obj.removeDuplicates(nums)#call the object function
result = nums[:k] + ["_"] * (len(nums) - k)#check
print("Output:", k, ", nums =", result)#print value
