class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)#jsut create for length
        for i in range(n):#check all numbers in the arrray
            index = abs(nums[i]) - 1#abs use for negative numbers control
            if nums[index] > 0:
                nums[index] = -nums[index]
        result = []#result store in the list
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)#append use for list
        return result
# Test
nums = [1, 2, 3, 4, 7]
obj = Solution()
print(obj.findDisappearedNumbers(nums))  # আউটপুট: [5, 6]