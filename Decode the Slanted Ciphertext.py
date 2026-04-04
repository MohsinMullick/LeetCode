class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        if not encodedText:
            return ""

        cols = len(encodedText) // rows
        result = []

        for c in range(cols):
            i = 0
            j = c
            while i < rows and j < cols:
                result.append(encodedText[i * cols + j])
                i += 1
                j += 1

        return "".join(result).rstrip()