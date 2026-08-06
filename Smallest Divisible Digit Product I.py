class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def digit_product(num):
            product = 1
            for ch in str(num):
                product *= int(ch)
            return product

        num = n
        while True:
            if digit_product(num) % t == 0:
                return num
            num += 1