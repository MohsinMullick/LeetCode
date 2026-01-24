class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]  # Row 0
        prev_row = [1]  # First row
        for i in range(1, rowIndex + 1):
            row = [1]  # First element
            for j in range(1, i):
                row.append(prev_row[j-1] + prev_row[j])  # Middle elements
            row.append(1)  # Last element
            prev_row = row  # Update for next row
        return prev_row
numRows = 4
obj = Solution()
array = obj.getRow(numRows)
print(f"\nFull triangle:{array}")
