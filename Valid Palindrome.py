class Solution(object):
    def isPalindrome(self, s):
        left = 0  # start index 0
        right = len(s) - 1  # end index [just use this two line two pointer technique]
        while left < right:  # use main two pointer
            while left < right and not s[left].isalnum():  # Two pointer + filtering on the fly
                left += 1
            while left < right and not s[right].isalnum():  # Two pointer + filtering on the fly
                right -= 1  # FIXED (was left -= 1)
            if s[left].lower() != s[right].lower():  # check all character lower
                return False
            left += 1
            right -= 1
        return True

s = " a man "
obj = Solution()
array = obj.isPalindrome(s)  # FIXED (method name correct)
print(array)