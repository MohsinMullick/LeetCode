class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])

        def flood(r, c):
            stack = [(r, c)]
            grid[r][c] = 1
            while stack:
                x, y = stack.pop()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        stack.append((nx, ny))


        for i in range(rows):
            for j in range(cols):
                if (i in (0, rows - 1) or j in (0, cols - 1)) and grid[i][j] == 0:
                    flood(i, j)


        count = 0
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if grid[i][j] == 0:
                    count += 1
                    flood(i, j)

        return count