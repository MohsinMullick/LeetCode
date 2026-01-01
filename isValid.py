"""
. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "()[]{}"
Output: true
Example 3:
Input: s = "(]"
Output: false
Example 4:
Input: s = "([])"
Output: true
Example 5:
Input: s = "([)]"
Output: false
Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution(object):#create class named Solution
    def isValid(self, s):#create method
        stack = []#when we need sequential all  elements then i use  stack
        mapping = {")": "(", "}": "{", "]": "["}#just maintain or finding relations
        for i in s:#loop continuously first bracket to last bracket checks
            if i in mapping.values():  # opening brackets stores
                stack.append(i)#all current brackets
            elif i in mapping:  # closing brackets
                if not stack or stack[-1] != mapping[i]:#condition false or empty check
                    return False
                stack.pop()
            else:  # invalid character
                return False

        return not stack  # True if stack is empty, else False
solve = Solution()
result = solve.isValid("(){}[]")  # input must be a single string, not separate characters
print(result)
