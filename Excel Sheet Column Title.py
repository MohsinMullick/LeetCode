class Solution(object):
    def convertToTitle(self,columnNumber):
        result=""#create empty string
        while columnNumber>0:#create logic because until this loop continue when convert 0
            columnNumber-=1#every iteration  1 decrease because python default 0
            remainder=columnNumber%26#division return the last value or digit
            result=chr(remainder+ord('A'))+result#thsi line most important because ASCII NUMBER convert chr
            columnNumber//=26#floor division that means division number cancel other numbers action
        return result#return the result

columnNumber = 1
obj=Solution()
array=obj.convertToTitle(columnNumber)
print(array)