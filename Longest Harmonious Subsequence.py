class Solution():
    def findLHS(self,nums):
        fre={}#create dictionary and every value store how times
        for num in nums:#traverse
            if num in fre:#check the dictionary
                fre[num]+=1#if same value then count from dictionary
            else:
                fre[num]=1
        answer=0
        for x in fre:
            if x+1 in fre:
                answer=max(answer,fre[x]+fre[x+1])
        return answer
nums=[1,3,2,2,5,2,3,7]
obj=Solution()
array=obj.findLHS(nums)
print(array)