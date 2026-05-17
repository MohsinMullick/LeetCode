class Solution(object):
    def canReach(self, arr, start):
        visited = set()
        stack = [start]

        while stack:
            i = stack.pop()

            if arr[i] == 0:
                return True

            if i in visited:
                continue
            visited.add(i)

            for next_i in (i + arr[i], i - arr[i]):
                if 0 <= next_i < len(arr) and next_i not in visited:
                    stack.append(next_i)

        return False