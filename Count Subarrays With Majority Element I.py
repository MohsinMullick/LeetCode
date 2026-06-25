class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        # Convert to +1/-1
        arr = [1 if x == target else -1 for x in nums]

        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + arr[i - 1]

        # Fenwick Tree (Binary Indexed Tree) setup
        offset = n
        max_val = 2 * n + 1
        tree = [0] * (max_val + 2)

        def update(idx, val):
            while idx <= max_val:
                tree[idx] += val
                idx += idx & -idx

        def query(idx):
            res = 0
            while idx > 0:
                res += tree[idx]
                idx -= idx & -idx
            return res

        count = 0
        # Insert prefix[0] = 0
        mapped = prefix[0] + offset + 1
        update(mapped, 1)

        for j in range(1, n + 1):
            p = prefix[j]
            # Count previous prefixes < p
            count += query(p + offset)  # up to mapped(p) - 1
            # Insert current prefix
            update(p + offset + 1, 1)

        return count