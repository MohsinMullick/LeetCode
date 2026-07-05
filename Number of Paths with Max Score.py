class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        if not board or not board[0]:
            return [0, 0]
        n = len(board)
        MOD = 10 ** 9 + 7
        # dp[i][j][0]: max score from (i,j) to E? No, from S to (i,j) but since filling reverse
        # We'll use dp for max score reaching (i,j) from S (bottom right)
        dp = [[-1] * n for _ in range(n)]  # max score
        count = [[0] * n for _ in range(n)]  # number of ways

        # base: S
        dp[n - 1][n - 1] = 0
        count[n - 1][n - 1] = 1

        directions = [(0, 1), (1, 0), (1, 1)]  # right, down, down-right (incoming)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] in 'XS':
                    continue
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and dp[ni][nj] != -1:
                        new_score = dp[ni][nj]
                        if new_score > dp[i][j]:
                            dp[i][j] = new_score
                            count[i][j] = count[ni][nj]
                        elif new_score == dp[i][j]:
                            count[i][j] = (count[i][j] + count[ni][nj]) % MOD

                if dp[i][j] != -1 and board[i][j] != 'E':
                    digit = int(board[i][j]) if board[i][j].isdigit() else 0
                    dp[i][j] += digit

        if dp[0][0] == -1:
            return [0, 0]
        return [dp[0][0], count[0][0]]