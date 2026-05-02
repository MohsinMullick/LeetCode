class Solution(object):
    def rotatedDigits(self, n):
        valid_same = {'0', '1', '8'}
        valid_diff = {'2', '5', '6', '9'}

        count = 0

        for num in range(1, n + 1):
            s = str(num)
            is_valid = True
            is_different = False

            for ch in s:
                if ch in valid_diff:
                    is_different = True
                elif ch not in valid_same:
                    is_valid = False
                    break

            if is_valid and is_different:
                count += 1

        return count