from sortedcontainers import SortedList
class Solution(object):
    def getResults(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Find max position for discretization
        max_pos = 0
        for q in queries:
            if q[0] == 1:
                max_pos = max(max_pos, q[1])
            else:
                max_pos = max(max_pos, q[1])

        # SortedList with all obstacles including sentinels
        obstacles = SortedList([0, max_pos + 1])

        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        # Fenwick Tree for max gap, using positions directly since we use index in SortedList carefully
        # Better to use coordinate compression on all relevant positions
        all_pos = sorted(set(obstacles))
        rank = {val: idx + 1 for idx, val in enumerate(all_pos)}
        m = len(all_pos)

        class Fenwick:
            def __init__(self, size):
                self.tree = [0] * (size + 2)

            def update(self, idx, val):
                while idx < len(self.tree):
                    self.tree[idx] = max(self.tree[idx], val)
                    idx += idx & -idx

            def query(self, idx):
                res = 0
                while idx > 0:
                    res = max(res, self.tree[idx])
                    idx -= idx & -idx
                return res

        ft = Fenwick(m + 1)

        # Build initial gaps with all obstacles
        for i in range(1, len(obstacles)):
            left = obstacles[i - 1]
            right = obstacles[i]
            gap = right - left
            r = rank[left]
            ft.update(r, gap)

        # Now process in reverse
        ans = []
        for q in reversed(queries):
            if q[0] == 1:
                # Undo addition: remove obstacle and merge gap
                x = q[1]
                idx = obstacles.index(x)
                prev = obstacles[idx - 1]
                nxt = obstacles[idx + 1]

                obstacles.remove(x)

                # Update the new merged gap
                new_gap = nxt - prev
                r_prev = rank[prev]
                ft.update(r_prev, new_gap)
            else:
                # Type 2 query
                x, sz = q[1], q[2]
                # Find largest obstacle position <= x
                idx = obstacles.bisect_right(x) - 1
                prev_pos = obstacles[idx]

                # Max gap up to prev_pos
                r_prev = rank[prev_pos]
                max_gap_so_far = ft.query(r_prev)

                # Gap from last obstacle to x
                gap_to_x = x - prev_pos

                can = max_gap_so_far >= sz or gap_to_x >= sz
                ans.append(can)

        return ans[::-1]