"""
Given an integer x, return true if x is a palindrome, and false otherwise.
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Constraints:
-231 <= x <= 231 - 1
"""
from operator import truediv


class Solution(object):#create class named solution
    def isPalindrome(self,x):#create method with given variable x
        x_str=str(x)#convert to the string because string easily reversed
        if x_str==x_str[::-1]:#now condition for reverse
            return True#if that numbers palindrome return value true
        else:
            return False#otherwise false

solve = Solution()#objfect create (instance)
results = solve.isPalindrome(121)#call the method
print(results)#print results
