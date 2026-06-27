from collections import Counter
import math

class Solution(object):
    def maximumLength(self, nums):
        freq = Counter(nums)
        if not freq:
            return 0
        max_len = 0
        # Handle 1 separately (all 1s form valid patterns of any odd length)
        f1 = freq.get(1, 0)
        if f1 > 0:
            odd_len = f1 if f1 % 2 == 1 else f1 - 1
            max_len = max(max_len, odd_len)
        # For other numbers, try each as potential middle and extend downward
        for num in list(freq.keys()):
            if num == 1:
                continue
            current = num
            length = 1
            while True:
                s = int(math.sqrt(current))
                if s * s != current:
                    # Check s+1 in case of floating point precision
                    if (s + 1) * (s + 1) == current:
                        s += 1
                    else:
                        break
                if s not in freq or freq[s] < 2:
                    break
                length += 2
                current = s
            max_len = max(max_len, length)
        # Singles are covered implicitly (max_len at least 1 if elements exist)
        if max_len == 0 and len(nums) > 0:
            max_len = 1
        return max_len