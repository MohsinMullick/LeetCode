from bisect import bisect_left

class Solution(object):
    def maximumWeight(self, intervals):
        n = len(intervals)
        order = sorted(range(n), key=lambda i: intervals[i][1])
        starts = [intervals[i][0] for i in order]
        ends = [intervals[i][1] for i in order]
        wts = [intervals[i][2] for i in order]
        prev = [bisect_left(ends, starts[i], 0, i) for i in range(n)]
        f = [[(0, ())] * 5 for _ in range(n + 1)]
        for i in range(1, n + 1):
            j = i - 1
            for k in range(1, 5):
                skip = f[i - 1][k]
                base_w, base_idx = f[prev[j]][k - 1]
                take_w = base_w + wts[j]
                take_idx = tuple(sorted(base_idx + (order[j],)))
                take = (take_w, take_idx)
                if take_w > skip[0]:
                    f[i][k] = take
                elif take_w < skip[0]:
                    f[i][k] = skip
                else:
                    f[i][k] = take if take_idx < skip[1] else skip
        return list(f[n][4][1])