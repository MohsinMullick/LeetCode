class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []#return empty
        triangle = [[1]]  # first row
        for i in range(1, numRows):
            row = [1]  # first element
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])  # middle elements
            row.append(1)  # last element
            triangle.append(row)  # append complete row
        return triangle

numRows = 4
obj = Solution()
array = obj.generate(numRows)
print(f"Pascal's Triangle with {numRows} rows:")
print("-----------------------------")
for i, row in enumerate(array, 1):
    print(f"Row {i-1}: {row}")

print("\nFull triangle:")
for row in array:
    # center-align each row (simple version)
    print(" " * (numRows - len(row)), end="")
    print(*row)
