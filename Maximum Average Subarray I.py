class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum=sum(nums[:k])
        max_sum=window_sum
        for i in range(k,len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum=max(max_sum,window_sum)
        return max_sum / 1.0 / k
nums = [1,12,-5,-6,50,3]
k = 4
obj=Solution()
array=obj.findMaxAverage(nums,k)
print(array)