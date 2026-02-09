class Solution():
    def canPlaceFlowers(self,flowerbed,n):
        length=len(flowerbed)#jsut take the flowerbed element like [1,0,1] total element=3
        for i in range(length):#traverse all element
            if flowerbed[i]==0:#this condition check which index 0
                left_empty=(i==0 or flowerbed[i-1]==0)#i-1 means python start 0 so i-1 use
                right_empty=(i==length-1 or flowerbed[i+1]==0)
                if left_empty and right_empty:
                    flowerbed[i]=1
                    n-=1
                    if n<=0:
                        return True
        return n<=0
flowerbed = [1,0,0,0,1]
n = 1
obj=Solution()
array=obj.canPlaceFlowers(flowerbed,n)
print(array)
