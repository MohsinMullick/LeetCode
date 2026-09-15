class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        dp = [0] * (n + 1)  # dp[i] = max non-overlapping palindromic substrings of length >= k in s[:i]

        def is_pal(l, r):  # check s[l:r] is palindrome
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]  # option: don't end a palindrome at i
            # Key insight: if a palindrome of length >= k ending at i exists,
            # one of length exactly k or k+1 also exists (strip 2 chars at a time
            # from a longer palindrome and it stays a palindrome). Checking only
            # these two shortest lengths is both sufficient and optimal (greedy:
            # shorter palindrome leaves more room for future ones).
            for length in (k, k + 1):
                j = i - length
                if j >= 0 and is_pal(j, i - 1):
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1

        return dp[n]