class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 10 ** 9 + 7
        k = r - l + 1

        if n == 1:
            return k % MOD

        # State: [up[0..k-1], dn[0..k-1]], size = 2k
        # up[j] -> new_dn[i] for all i < j  (up[j] contributes to dn[i] where i<j)
        # dn[j] -> new_up[i] for all i > j  (dn[j] contributes to up[i] where i>j)

        size = 2 * k

        def mat_mul(A, B):
            n = len(A)
            C = [[0] * n for _ in range(n)]
            for i in range(n):
                for l_ in range(n):
                    if A[i][l_] == 0:
                        continue
                    for j in range(n):
                        C[i][j] = (C[i][j] + A[i][l_] * B[l_][j]) % MOD
            return C

        def mat_pow(M, p):
            # Identity matrix
            n = len(M)
            result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
            while p:
                if p & 1:
                    result = mat_mul(result, M)
                M = mat_mul(M, M)
                p >>= 1
            return result

        # Build transition matrix T of size 2k x 2k
        # Index mapping: up[j] -> index j, dn[j] -> index k+j
        T = [[0] * size for _ in range(size)]

        for j in range(k):
            # dn[j] (index k+j) contributes to new_up[i] for all i > j
            for i in range(j + 1, k):
                T[i][k + j] = 1  # new_up[i] += dn[j]

            # up[j] (index j) contributes to new_dn[i] for all i < j
            for i in range(0, j):
                T[k + i][j] = 1  # new_dn[i] += up[j]

        # Initial state vector (after 2 elements placed)
        # up[j] = j, dn[j] = k-1-j
        state = [0] * size
        for j in range(k):
            state[j] = j  # up[j]
            state[k + j] = k - 1 - j  # dn[j]

        # Apply T^(n-2) to state
        Tp = mat_pow(T, n - 2)

        # Multiply matrix * vector
        new_state = [0] * size
        for i in range(size):
            for j in range(size):
                new_state[i] = (new_state[i] + Tp[i][j] * state[j]) % MOD

        return sum(new_state) % MOD