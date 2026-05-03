class Solution:
    def flipAndInvertImage(self, image):
        n = len(image)

        for row in image:
            left, right = 0, n - 1

            while left <= right:
                row[left], row[right] = row[right] ^ 1, row[left] ^ 1
                left += 1
                right -= 1

        return image