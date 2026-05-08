from collections import deque, defaultdict
import math

class Solution(object):
    def minJumps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        # Check prime
        def isPrime(x):
            if x < 2:
                return False

            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    return False

            return True

        # Store indices divisible by prime factor
        mp = defaultdict(list)

        for i, val in enumerate(nums):
            temp = val
            d = 2

            while d * d <= temp:
                if temp % d == 0:
                    mp[d].append(i)

                    while temp % d == 0:
                        temp //= d

                d += 1

            if temp > 1:
                mp[temp].append(i)

        # BFS
        q = deque([0])
        visited = [False] * n
        visited[0] = True

        steps = 0
        usedPrime = set()

        while q:

            for _ in range(len(q)):

                i = q.popleft()

                if i == n - 1:
                    return steps

                # Left
                if i - 1 >= 0 and not visited[i - 1]:
                    visited[i - 1] = True
                    q.append(i - 1)

                # Right
                if i + 1 < n and not visited[i + 1]:
                    visited[i + 1] = True
                    q.append(i + 1)

                # Teleport
                val = nums[i]

                if isPrime(val) and val not in usedPrime:

                    for nxt in mp[val]:

                        if not visited[nxt]:
                            visited[nxt] = True
                            q.append(nxt)

                    usedPrime.add(val)

            steps += 1

        return -1