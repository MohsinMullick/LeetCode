class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        # forward graph: a -> [b1, b2, ...] (a calls b1, b2...)
        graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)
        # step 1: k theke forward BFS/DFS - k ja call kore (direct/indirect) sob suspicious
        suspicious = {k}
        stack = [k]
        while stack:
            cur = stack.pop()
            for callee in graph[cur]:
                if callee not in suspicious:
                    suspicious.add(callee)
                    stack.append(callee)
        # step 2: consistency check - kono NON-suspicious method jodi
        # suspicious method-ke call kore, tahole remove kora jabe na
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))  # remove kora jabe na, sob return kori
        # step 3: sob safe (non-suspicious) methods return kori
        return [i for i in range(n) if i not in suspicious]