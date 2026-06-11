class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        if not edges:
            return 0
        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        from collections import deque
        q = deque([1])
        seen = {1}
        step = 0
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                for v in graph[u]:
                    if v not in seen:
                        q.append(v)
                        seen.add(v)
            step += 1
        # step is max_depth + 1 (levels)
        # ways = 2^(max_depth_edges - 1)
        if step <= 1:
            return 0
        return pow(2, step - 2, MOD)