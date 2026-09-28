class Solution(object):
    def resultArray(self, nums, k):
        res = [0] * k
        cnt = [0] * k

        for a in nums:
            new = [0] * k
            new[a % k] += 1
            for r in range(k):
                if cnt[r]:
                    new[(r * a) % k] += cnt[r]
            for r in range(k):
                res[r] += new[r]
            cnt = new

        return res