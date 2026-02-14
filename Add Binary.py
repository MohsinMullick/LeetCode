class Solution(object):
    def addBinary(self,a,b):
        i=len(a)-1#from the i end index
        j=len(b)-1#from the j end index
        carry=0
        result=" "
        while i>=0 or j>=0 or carry:
            total=carry

            if i>=0:
                total+=int(a[i])
                i-=1

            if j>=0:
                total+=int(b[i])
                j-=1
            result=str(total%2)+result
            carry=total//2
        return result
a = "11"
b = "1"
obj=Solution()
array=obj.addBinary(a,b)
print(array)