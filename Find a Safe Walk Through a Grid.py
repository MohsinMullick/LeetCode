from collections import deque


class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])

        # dist[i][j] = minimum total damage (number of unsafe cells) taken to reach (i, j)
        INF = float('inf')
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = grid[0][0]  # damage from starting cell itself

        dq = deque([(0, 0)])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while dq:
            x, y = dq.popleft()
            d = dist[x][y]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    cost = grid[nx][ny]  # 1 if unsafe, 0 if safe
                    nd = d + cost
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        if cost == 0:
                            dq.appendleft((nx, ny))  # 0-weight edge -> front
                        else:
                            dq.append((nx, ny))  # 1-weight edge -> back

        return health - dist[m - 1][n - 1] >= 1