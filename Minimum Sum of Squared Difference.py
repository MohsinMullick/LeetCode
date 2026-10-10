class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diff) <= k:
            return 0

        m = max(diff)
        cnt = [0] * (m + 1)
        for d in diff:
            cnt[d] += 1

        for v in range(m, 0, -1):
            c = cnt[v]
            if c == 0:
                continue
            if k >= c:
                cnt[v - 1] += c
                cnt[v] = 0
                k -= c
            else:
                cnt[v - 1] += k
                cnt[v] = c - k
                k = 0
                break

        return sum(v * v * c for v, c in enumerate(cnt))