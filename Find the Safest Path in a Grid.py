from collections import deque
import sys


class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0

        # Step 1: Multi-source BFS to compute min distance to thief for each cell
        dist = [[sys.maxsize] * n for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # Step 2: Binary search on safeness factor
        left, right = 0, dist[0][0]  # max possible is limited by start cell
        while left <= right:
            mid = (left + right) // 2
            if self._can_reach(dist, mid, n):
                left = mid + 1
            else:
                right = mid - 1
        return right

    def _can_reach(self, dist, safe, n):
        if dist[0][0] < safe or dist[n - 1][n - 1] < safe:
            return False
        visited = [[False] * n for _ in range(n)]
        q = deque([(0, 0)])
        visited[0][0] = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            r, c = q.popleft()
            if r == n - 1 and c == n - 1:
                return True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and dist[nr][nc] >= safe:
                    visited[nr][nc] = True
                    q.append((nr, nc))
        return False