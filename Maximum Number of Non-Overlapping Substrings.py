class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        intervals = []
        for i in range(n):
            c = s[i]
            if first[c] != i:
                continue  # only start an interval at a character's first occurrence

            start, end = i, last[c]
            j = start
            valid = True
            while j <= end:
                cj = s[j]
                if first[cj] < start:
                    valid = False
                    break
                end = max(end, last[cj])
                j += 1

            if valid:
                intervals.append((start, end))

        # Pick minimum-length (smallest-end) non-overlapping intervals greedily
        intervals.sort(key=lambda x: x[1])
        res = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                res.append(s[start:end + 1])
                prev_end = end

        return res