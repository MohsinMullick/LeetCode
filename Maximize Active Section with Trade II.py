from bisect import bisect_left, bisect_right


class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        total_ones = s.count("1")
        n = len(s)

        # Store every maximal zero block.
        starts = []
        ends = []
        lengths = []

        i = 0
        while i < n:
            if s[i] == "1":
                i += 1
                continue

            j = i
            while j + 1 < n and s[j + 1] == "0":
                j += 1

            starts.append(i)
            ends.append(j)
            lengths.append(j - i + 1)
            i = j + 1

        zero_blocks = len(lengths)

        # A trade requires at least two zero blocks with a one block between them.
        if zero_blocks < 2:
            return [total_ones] * len(queries)

        # pair_gain[i] is the gain obtained by merging zero blocks i and i + 1.
        pair_gain = [
            lengths[i] + lengths[i + 1]
            for i in range(zero_blocks - 1)
        ]

        # Iterative segment tree for range maximum queries.
        size = 1
        while size < len(pair_gain):
            size <<= 1

        tree = [0] * (2 * size)

        for i, value in enumerate(pair_gain):
            tree[size + i] = value

        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])

        def range_max(left, right):
            """Maximum pair gain on the inclusive range [left, right]."""
            if left > right:
                return 0

            left += size
            right += size
            result = 0

            while left <= right:
                if left & 1:
                    result = max(result, tree[left])
                    left += 1

                if not (right & 1):
                    result = max(result, tree[right])
                    right -= 1

                left >>= 1
                right >>= 1

            return result

        def clipped_length(block, left, right):
            """Length of a zero block that lies inside [left, right]."""
            return (
                min(ends[block], right)
                - max(starts[block], left)
                + 1
            )

        answer = []

        for left, right in queries:
            # First zero block intersecting the query.
            first = bisect_left(ends, left)

            # Last zero block intersecting the query.
            last = bisect_right(starts, right) - 1

            # Fewer than two zero blocks means no valid trade.
            if first >= last:
                answer.append(total_ones)
                continue

            # Pair involving the potentially clipped left boundary block.
            best_gain = (
                clipped_length(first, left, right)
                + clipped_length(first + 1, left, right)
            )

            # Pair involving the potentially clipped right boundary block.
            best_gain = max(
                best_gain,
                clipped_length(last - 1, left, right)
                + clipped_length(last, left, right)
            )

            # Pairs completely contained inside the query.
            best_gain = max(
                best_gain,
                range_max(first + 1, last - 2)
            )

            answer.append(total_ones + best_gain)

        return answer