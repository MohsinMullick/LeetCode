class NumArray(object):
    def __init__(self, nums):#create constraint
        self.prefix = []#empty
        current_sum = 0#current_value 0
        for num in nums:
            current_sum += num
            self.prefix.append(current_sum)
    def sumRange(self, left, right):
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]
# -------- MAIN PART --------
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))