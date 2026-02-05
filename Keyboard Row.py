class Solution(object):
    def findWords(self,words):
        r1=set("qwertyuiop")#first row from keyboard
        r2=set("asdfghjkl")#second row from keyboard
        r3=set("zxcvbnm")#third row from keyboard
        result=[]#store character create list
        for word in words:#traverse
            w=word.lower()#all words lower case convert
            if w[0] in r1:#word first character which or where row included this line check
                r=r1
            elif w[0] in r2:
                r=r2
            else:
                r=r3
            if all(ch in r for ch in w):
                result.append(word)#if valid result list add
        return result

words=["Hello","Alaska","Dad","Peace"]
obj=Solution()
array=obj.findWords(words)
print(array)