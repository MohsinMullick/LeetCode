class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    def gcdOfStrings(self, str1, str2):
        # Step 1: check pattern compatibility
        if str1 + str2 != str2 + str1:
            return ""
        # Step 2: use custom gcd
        length = self.gcd(len(str1), len(str2))
        # Step 3: return base string
        return str1[:length]