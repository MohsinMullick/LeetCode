class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """

        def waviness(x):
            if x == 0:
                return 0
            digits = []
            while x > 0:
                digits.append(x % 10)
                x //= 10
            digits = digits[::-1]  # reverse to get correct order
            n = len(digits)
            if n < 3:
                return 0
            count = 0
            for i in range(1, n - 1):
                if (digits[i] > digits[i - 1] and digits[i] > digits[i + 1]) or \
                        (digits[i] < digits[i - 1] and digits[i] < digits[i + 1]):
                    count += 1
            return count

        total = 0
        for num in range(num1, num2 + 1):
            total += waviness(num)
        return total