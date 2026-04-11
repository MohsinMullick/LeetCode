class Solution(object):
    def minimumDistance(self, nums):
        index_map = defaultdict(list)
        for i, num in enumerate(nums):
            index_map[num].append(i)
        result = float('inf')
        for indices in index_map.values():
            if len(indices) < 3:
                continue
            for i in range(len(indices) - 2):
                result = min(result, 2 * (indices[i + 2] - indices[i]))
        return result if result != float('inf') else -1