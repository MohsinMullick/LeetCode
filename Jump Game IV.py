from collections import defaultdict, deque
class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n == 1:
            return 0
        # Map each value to all indices that hold it
        value_to_indices = defaultdict(list)
        for i, val in enumerate(arr):
            value_to_indices[val].append(i)

        visited = {0}
        queue = deque([0])
        steps = 0

        while queue:
            steps += 1

            for _ in range(len(queue)):
                i = queue.popleft()

                neighbors = [i - 1, i + 1]
                neighbors += value_to_indices[arr[i]]

                for j in neighbors:
                    if j == n - 1:
                        return steps
                    if 0 <= j < n and j not in visited:
                        visited.add(j)
                        queue.append(j)

                # Delete after expanding so the group is never re-processed
                del value_to_indices[arr[i]]

        return -1