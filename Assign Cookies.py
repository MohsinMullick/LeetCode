class Solution(object):
    def findContentChildren(self,g,s):
        g.sort()#jsut for sorting
        s.sort()#just for sorting
        i=0#children pointer
        j=0#cookie pointer
        count=0#coutn cookies
        while i< len(g) and j <len(s):
            if s[j]>=g[i]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        return count
g = [1,2,3]
s = [1,1]
obj=Solution()
array=obj.findContentChildren(g,s)
print(array)
