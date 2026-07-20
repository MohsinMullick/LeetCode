class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])

        # Flatten the grid into a 1D list
        flat = [grid[i][j] for i in range(m) for j in range(n)]

        total = m * n
        k %= total  # no need to shift more than the total number of elements

        # Shift by rotating the flat list
        shifted = flat[-k:] + flat[:-k] if k != 0 else flat

        # Reshape back into 2D grid
        result = []
        for i in range(m):
            row = shifted[i * n: (i + 1) * n]
            result.append(row)

        return result