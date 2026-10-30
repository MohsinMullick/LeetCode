import heapq

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))

        INF = float('inf')
        # dist[node][run] : node
        dist = [[INF] * (k + 1) for _ in range(n)]

        if k < 1:
            return -1

        dist[0][1] = 0
        heap = [(0, 0, 1)]  # (cost, node, run)

        while heap:
            d, u, run = heapq.heappop(heap)
            if d > dist[u][run]:
                continue
            if u == n - 1:
                return d
            for v, w in graph[u]:
                new_run = run + 1 if labels[v] == labels[u] else 1
                if new_run > k:
                    continue
                nd = d + w
                if nd < dist[v][new_run]:
                    dist[v][new_run] = nd
                    heapq.heappush(heap, (nd, v, new_run))

        return -1