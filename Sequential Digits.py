class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        digits = "123456789"
        n = len(digits)
        result = []

        # length of low and high to know which window of lengths to check
        min_len = len(str(low))
        max_len = len(str(high))

        for length in range(min_len, max_len + 1):
            for start in range(0, n - length + 1):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    result.append(num)

        return result