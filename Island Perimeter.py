class Solution(object):
    def islandPerimeter(self, grid):
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4#says land

                    if i > 0 and grid[i-1][j] == 1:  # up
                        perimeter -= 1
                    if i < len(grid)-1 and grid[i+1][j] == 1:  # down
                        perimeter -= 1
                    if j > 0 and grid[i][j-1] == 1:  # left
                        perimeter -= 1
                    if j < len(grid[0])-1 and grid[i][j+1] == 1:  # right
                        perimeter -= 1
        return perimeter

grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
obj=Solution()
array=obj.islandPerimeter(grid)
print(array)


