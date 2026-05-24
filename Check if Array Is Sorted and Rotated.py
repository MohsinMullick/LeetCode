class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        n = len(arr)
        memo = [-1] * n

        # Precompute next greater or equal to left and right
        left_limit = [0] * n
        right_limit = [n - 1] * n

        # Next Greater or Equal to the Left
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            left_limit[i] = stack[-1] + 1 if stack else 0
            stack.append(i)

        # Next Greater or Equal to the Right
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] <= arr[i]:  # Note: <= for right
                stack.pop()
            right_limit[i] = stack[-1] - 1 if stack else n - 1
            stack.append(i)

        def dp(i):
            if memo[i] != -1:
                return memo[i]

            max_steps = 1

            # Right jumps
            farthest_right = min(i + d, right_limit[i])
            for j in range(i + 1, farthest_right + 1):
                if arr[j] < arr[i]:
                    max_steps = max(max_steps, 1 + dp(j))

            # Left jumps
            farthest_left = max(i - d, left_limit[i])
            for j in range(i - 1, farthest_left - 1, -1):
                if arr[j] < arr[i]:
                    max_steps = max(max_steps, 1 + dp(j))

            memo[i] = max_steps
            return max_steps

        result = 1
        for i in range(n):
            result = max(result, dp(i))

        return result