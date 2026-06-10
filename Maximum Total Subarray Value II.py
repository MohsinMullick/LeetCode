import heapq


class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        if k == 0:
            return 0

        # Compute log
        logn = 0
        while (1 << logn) <= n:
            logn += 1
        logn += 1  # extra safety

        # Sparse table for max and min
        st_max = [[0] * logn for _ in range(n)]
        st_min = [[0] * logn for _ in range(n)]

        for i in range(n):
            st_max[i][0] = nums[i]
            st_min[i][0] = nums[i]

        for j in range(1, logn):
            for i in range(n - (1 << j) + 1):
                st_max[i][j] = max(st_max[i][j - 1], st_max[i + (1 << (j - 1))][j - 1])
                st_min[i][j] = min(st_min[i][j - 1], st_min[i + (1 << (j - 1))][j - 1])

        def query_max(l, r):
            if l > r:
                return float('-inf')  # shouldn't happen
            length = r - l + 1
            k = 0
            while (1 << (k + 1)) <= length:
                k += 1
            return max(st_max[l][k], st_max[r - (1 << k) + 1][k])

        def query_min(l, r):
            if l > r:
                return float('inf')
            length = r - l + 1
            k = 0
            while (1 << (k + 1)) <= length:
                k += 1
            return min(st_min[l][k], st_min[r - (1 << k) + 1][k])

        # Max-heap: use negative value
        pq = []
        for l in range(n):
            val = query_max(l, n - 1) - query_min(l, n - 1)
            heapq.heappush(pq, (-val, l, n - 1))

        total = 0
        for _ in range(k):
            if not pq:
                break
            neg_val, l, r = heapq.heappop(pq)
            total -= neg_val
            if l < r:
                new_val = query_max(l, r - 1) - query_min(l, r - 1)
                heapq.heappush(pq, (-new_val, l, r - 1))

        return total
    