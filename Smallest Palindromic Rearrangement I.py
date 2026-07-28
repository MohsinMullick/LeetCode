class Solution {
public:
    string smallestPalindrome(string s) {
        int freq[26] = {0};
        for (char c : s) freq[c - 'a']++;

        int oddCount = 0;
        for (int i = 0; i < 26; i++) if (freq[i] % 2) oddCount++;
        if (oddCount > 1) return ""; // impossible case

        string half = "";
        char mid = 0;
        for (int i = 0; i < 26; i++) {
            half += string(freq[i] / 2, 'a' + i);
            if (freq[i] % 2) mid = 'a' + i;
        }

        string rev = half;
        reverse(rev.begin(), rev.end());

        return mid ? half + mid + rev : half + rev;
    }
};