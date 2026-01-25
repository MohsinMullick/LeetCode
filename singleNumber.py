class Solution(object):
    def singleNumber(self, nums):
        result = 0  # initial value
        for num in nums:
            result = result ^ num  # XOR operation
        return result
nums=[2,2,1]
obj=Solution()
array=obj.singleNumber(nums)
print(array)