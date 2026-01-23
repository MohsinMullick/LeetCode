"""
You are given a large integer represented as an integer array digits,
 where each digits[i] is the ith digit of the integer.
 The digits are ordered from most significant to least significant
 in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
"""
class Solution(object):#create class
    def plusOne(self,digits):#create function and digit's array like ...[1,2,3,4,5]
        n=len(digits)#array length

        for i in range((n-1),-1,-1):#n-1=last digits,-1 means start 0 and -1 means reverse direction
            if digits[i]<9:#if digits less than 9
                digits[i]+=1#if digits less than 9 then add +1 and return digits
                return digits#return digits
            digits[i]=0#if digits 0
        return[1]+digits#0+1
digits=[1,2,3,4,5,6]
obj=Solution()
array=obj.plusOne(digits)
print(f"1 add after digits: {array}")



