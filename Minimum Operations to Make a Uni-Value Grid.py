class Solution(object):
    def minOperations(self, grid, x):
        arr = []

        # flatten grid
        for row in grid:
            for val in row:
                arr.append(val)

        # check same remainder
        mod = arr[0] % x
        for val in arr:
            if val % x != mod:
                return -1

        # sort and find median
        arr.sort()
        median = arr[len(arr) // 2]

        # count operations
        ops = 0
        for val in arr:
            ops += abs(val - median) // x

        return ops