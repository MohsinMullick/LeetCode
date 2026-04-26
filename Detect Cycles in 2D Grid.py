class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        vis = [[False] * n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(x, y, px, py, ch):
            vis[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] != ch:
                        continue
                    if nx == px and ny == py:
                        continue

                    if vis[nx][ny]:
                        return True

                    # DFS continue
                    if dfs(nx, ny, x, y, ch):
                        return True

            return False

        for i in range(m):
            for j in range(n):
                if not vis[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True

        return False