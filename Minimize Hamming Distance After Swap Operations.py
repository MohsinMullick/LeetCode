class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)

        # Step 1: Union Find setup
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        # Step 2: Build connected components
        for a, b in allowedSwaps:
            union(a, b)

        # Step 3: Group indices by root
        from collections import defaultdict, Counter
        groups = defaultdict(list)

        for i in range(n):
            root = find(i)
            groups[root].append(i)

        # Step 4: Calculate minimum Hamming distance
        result = 0

        for indices in groups.values():
            count = Counter()

            # count source elements
            for i in indices:
                count[source[i]] += 1

            # match with target
            for i in indices:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    result += 1

        return result