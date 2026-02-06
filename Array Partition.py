class Solution(): #create the class
    def arrayPairSum(self,nums): #create function nums list and ->int return integer value
        nums.sort() #nums list ascending order
        t_sum=0#create variable
        for i in range(0,len(nums),2): #traverse and take two index step
            t_sum+=nums[i] #total sun
        return t_sum #return value
nums=[1,2,3,4]
obj=Solution()
array=obj.arrayPairSum(nums)
print(array)

