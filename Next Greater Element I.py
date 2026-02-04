class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []#store the next element which i got  don't find
        next_greater = {}
        # nums2 process
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        # remaining elements
        while stack:
            next_greater[stack.pop()] = -1
        # answer for nums1
        result = []
        for num in nums1:
            result.append(next_greater[num])
        return result
nums1 = [4,1,2]
nums2 = [1,3,4,2]

obj = Solution()
result = obj.nextGreaterElement(nums1,nums2)
print(result)
