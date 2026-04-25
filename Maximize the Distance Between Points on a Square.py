class Solution:
    def maxDistance(self, side, points, k):
        # Step 1: map 2D → 1D
        def map_point(x, y):
            if x == 0:
                return y
            elif y == side:
                return side + x
            elif x == side:
                return 3 * side - y
            else:  # y == 0
                return 4 * side - x

        arr = [map_point(x, y) for x, y in points]
        arr.sort()

        n = len(arr)
        perimeter = 4 * side

        # Step 2: binary search
        def can(d):
            # try every starting point
            for i in range(n):
                count = 1
                prev = arr[i]

                # greedy pick
                for j in range(i + 1, i + n):
                    curr = arr[j % n]

                    # handle circular
                    if j >= n:
                        curr += perimeter

                    if curr - prev >= d:
                        count += 1
                        prev = curr

                    if count >= k:
                        return True

            return False

        left, right = 0, perimeter

        while left < right:
            mid = (left + right + 1) // 2
            if can(mid):
                left = mid
            else:
                right = mid - 1

        return left