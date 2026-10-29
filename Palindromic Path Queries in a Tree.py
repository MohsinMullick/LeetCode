class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        LOG = max(1, n.bit_length())
        par = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        base = [0] * n
        cur = [1 << (ord(ch) - 97) for ch in s]

        base[0] = cur[0]
        it = [0] * n
        stack = [0]
        timer = 1
        while stack:
            u = stack[-1]
            if it[u] < len(adj[u]):
                v = adj[u][it[u]]
                it[u] += 1
                if v == par[u]:
                    continue
                par[v] = u
                depth[v] = depth[u] + 1
                base[v] = base[u] ^ cur[v]
                tin[v] = timer
                timer += 1
                stack.append(v)
            else:
                tout[u] = timer
                stack.pop()

        up = [par[:]]
        for k in range(1, LOG):
            prev = up[k - 1]
            up.append([prev[prev[v]] for v in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if (diff >> k) & 1:
                    u = up[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return par[u]

        bit = [0] * (n + 2)

        def add(i, x):
            i += 1
            while i <= n:
                bit[i] ^= x
                i += i & -i

        def pref(i):
            i += 1
            r = 0
            while i > 0:
                r ^= bit[i]
                i -= i & -i
            return r

        def pre(v):
            return base[v] ^ pref(tin[v])

        res = []
        for q in queries:
            p = q.split()
            if p[0] == "update":
                u = int(p[1])
                new = 1 << (ord(p[2]) - 97)
                d = cur[u] ^ new
                if d:
                    add(tin[u], d)
                    add(tout[u], d)
                    cur[u] = new
            else:
                u, v = int(p[1]), int(p[2])
                w = lca(u, v)
                mask = pre(u) ^ pre(v) ^ cur[w]
                res.append((mask & (mask - 1)) == 0)
        return res