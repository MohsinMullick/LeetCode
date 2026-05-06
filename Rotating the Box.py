class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        m = len(boxGrid)
        n = len(boxGrid[0])

        # Step 1: Apply gravity in each row
        for i in range(m):
            write = n - 1  # position where stones will settle

            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    write = j - 1  # reset after obstacle
                elif boxGrid[i][j] == '#':
                    boxGrid[i][j] = '.'
                    boxGrid[i][write] = '#'
                    write -= 1

        # Step 2: Rotate 90 degrees clockwise
        res = [["." for _ in range(m)] for _ in range(n)]

        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = boxGrid[i][j]

        return res