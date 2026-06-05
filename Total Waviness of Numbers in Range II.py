class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """

        def count(x):
            if x <= 0:
                return 0
            d = []
            tmp = x
            while tmp:
                d.append(tmp % 10)
                tmp //= 10
            d.reverse()

            memo = {}

            def solve(pos, sum_w, p2, p1, small, nz):
                if pos == len(d):
                    return sum_w
                key = (pos, sum_w, p2, p1, small, nz)
                if key in memo:
                    return memo[key]
                lim = 9 if small else d[pos]
                res = 0
                for i in range(lim + 1):
                    nsmall = small or (i < d[pos])
                    nnz = nz or (i != 0)
                    if nnz:
                        np2 = p1
                        np1 = i
                        nsum = sum_w
                        if p2 != 10 and p1 != 10:
                            if (p2 < p1 and p1 > i) or (p2 > p1 and p1 < i):
                                nsum += 1
                        res += solve(pos + 1, nsum, np2, np1, nsmall, nnz)
                    else:
                        res += solve(pos + 1, sum_w, p2, p1, nsmall, nnz)
                memo[key] = res
                return res

            return solve(0, 0, 10, 10, False, False)

        return count(num2) - count(num1 - 1)