class Solution():
    def summaryRange(self,nums):
        if not nums:#maintain for error because if sometimes empty array entry then output error
            return []


        result=[]#all value store
        start=nums[0]#start value 0
        pre=nums[0]#previous value 0 so current value 0


        for i in range(1,len(nums)):#traverse all values
            #if range not same range break because consecutive numbers find
            if nums[i]==pre+1:#like i=1,previous i=0+1=1 so nums[i]== previous
                pre=nums[i]
            else:
                #check for single number or range
                if start==pre:
                    result.append(str(start))#.append use list element add
                else:
                    result.append(str(start)+ "->"+ str(pre))#.append use list element add
                    start=nums[i]
                    pre=nums[i]

        # this condition use for last range missing
        if start==pre:
            result.append(str(start))
        else:
            result.append(str(start)+ "->"+ str(pre))#.append use list element add
        return result

#----------MAin----------
nums = [0, 1, 2, 4, 5, 7]
obj = Solution()
print(obj.summaryRange(nums))







