class Solution(object):
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        # Directions mapping
        dirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        # Opposite direction
        opposite = {
            (0, -1): (0, 1),
            (0, 1): (0, -1),
            (-1, 0): (1, 0),
            (1, 0): (-1, 0)
        }

        from collections import deque
        queue = deque([(0, 0)])
        visited = set([(0, 0)])

        while queue:
            x, y = queue.popleft()

            # Reached destination
            if x == m - 1 and y == n - 1:
                return True

            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    # Check if neighbor connects back
                    if opposite[(dx, dy)] in dirs[grid[nx][ny]]:
                        visited.add((nx, ny))
                        queue.append((nx, ny))

        return False