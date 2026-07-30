class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26
        for c in word:
            freq[ord(c) - ord('a')] += 1

        freq.sort(reverse=True)

        total_pushes = 0
        for i in range(26):
            if freq[i] == 0:
                break
            push_cost = (i // 8) + 1
            total_pushes += freq[i] * push_cost

        return total_pushes

if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumPushes("abcde"))  # 5
    print(sol.minimumPushes("xyzxyzxyzxyz"))  # 12
    print(sol.minimumPushes("aabbccddeeffgghhiiiiii"))  # 24