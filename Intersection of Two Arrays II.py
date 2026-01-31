class Solution(object):
    def intersect(self,nums1,nums2):
        dic={}#create dictionary for count duplicate value
        result=[]#create empty list

        for i in nums1:#nusm1 all value check
            if i in dic:#check the duplicate value for dictionary
                dic[i]+=1# f find the same value increase the 1 or count 1
            else:
                dic[i]=1#otherswise not increase
        for i in nums2:#nusm2 all element check
            if i in dic and dic[i]>0:#both condition are true
                result.append(i)
                dic[i]-=1#for the duplicate control
        return result
nums1=[1,2,2,3]
nums2=[2,2]
obj=Solution()
array=obj.intersect(nums1,nums2)
print(array)