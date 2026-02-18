class Solution(object):
    def titleToNumber(self,columnTitle):
        result=0
        for ch in columnTitle:
            result = result * 26 + (ord(ch) - ord('A') + 1)
        return result
columnTitle="A"
obj=Solution()
string=obj.titleToNumber(columnTitle)
print(string)