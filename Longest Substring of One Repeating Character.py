import sys

class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n = len(s)
        s = list(s)  # mutable

        # segment tree arrays
        pref = [0] * (4 * n)
        suf  = [0] * (4 * n)
        best = [0] * (4 * n)
        lch  = [''] * (4 * n)
        rch  = [''] * (4 * n)

        def pull(node, l, mid, r):
            left, right = 2 * node, 2 * node + 1
            leftSize = mid - l + 1
            rightSize = r - mid

            lch[node] = lch[left]
            rch[node] = rch[right]

            pref[node] = pref[left]
            if pref[left] == leftSize and rch[left] == lch[right]:
                pref[node] += pref[right]

            suf[node] = suf[right]
            if suf[right] == rightSize and rch[left] == lch[right]:
                suf[node] += suf[left]

            best[node] = max(best[left], best[right])
            if rch[left] == lch[right]:
                best[node] = max(best[node], suf[left] + pref[right])

        def build(node, l, r):
            if l == r:
                lch[node] = rch[node] = s[l]
                pref[node] = suf[node] = best[node] = 1
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            pull(node, l, mid, r)

        def update(node, l, r, idx, ch):
            if l == r:
                lch[node] = rch[node] = ch
                pref[node] = suf[node] = best[node] = 1
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, r, idx, ch)
            pull(node, l, mid, r)

        sys.setrecursionlimit(max(10000, 4 * n + 10))

        build(1, 0, n - 1)

        ans = []
        for ch, idx in zip(queryCharacters, queryIndices):
            if s[idx] != ch:
                s[idx] = ch
                update(1, 0, n - 1, idx, ch)
            ans.append(best[1])

        return ans