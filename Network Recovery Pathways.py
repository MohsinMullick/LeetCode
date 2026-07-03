from collections import deque


class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)
        adj = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v, c in edges:
            adj[u].append((v, c))
            indeg[v] += 1

        # topological order (graph is a DAG)
        order = []
        indeg_copy = indeg[:]
        dq = deque([i for i in range(n) if indeg_copy[i] == 0])
        while dq:
            u = dq.popleft()
            order.append(u)
            for v, c in adj[u]:
                indeg_copy[v] -= 1
                if indeg_copy[v] == 0:
                    dq.append(v)

        costs = sorted(set(c for _, _, c in edges))

        def check(mid):
            INF = float('inf')
            dist = [INF] * n
            dist[0] = 0
            for u in order:
                if dist[u] == INF or not online[u]:
                    continue
                for v, c in adj[u]:
                    if c >= mid and online[v] and dist[u] + c < dist[v]:
                        dist[v] = dist[u] + c
            return dist[n - 1] <= k

        lo, hi = 0, len(costs) - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(costs[mid]):
                ans = costs[mid]
                lo = mid + 1
            else:
                hi = mid - 1
        return ans