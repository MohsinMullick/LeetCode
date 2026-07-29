class Solution {
public:
    string smallestPalindrome(string s, int k) {
        int n = s.size();
        vector<long long> freq(26, 0);
        for (char c : s) freq[c - 'a']++;

        int oddCount = 0, oddChar = -1;
        for (int i = 0; i < 26; i++) {
            if (freq[i] % 2 == 1) {
                oddCount++;
                oddChar = i;
            }
        }
        if (oddCount > 1) return ""; // palindrome possible-ই না

        vector<long long> half(26, 0);
        long long halfLen = 0;
        for (int i = 0; i < 26; i++) {
            half[i] = freq[i] / 2;
            halfLen += half[i];
        }

        const long long CAP = 3000000000LL; // int max (~2.147e9) er cheye beshi

        // counts multiset diye koyta distinct permutation hobe, ta capped value hishebe return kore
        auto countPerms = [&](vector<long long>& counts, long long length) -> long long {
            __int128 result = 1;
            long long remaining = length;
            for (int i = 0; i < 26 && result <= (__int128)CAP; i++) {
                long long c = counts[i];
                if (c == 0) continue;
                __int128 comb = 1;
                for (long long j = 1; j <= c; j++) {
                    comb = comb * (remaining - c + j);
                    comb /= j;
                    if (comb > (__int128)CAP) break; // early exit, overflow thekano
                }
                if (comb > (__int128)CAP) comb = (__int128)CAP + 1;
                result *= comb;
                remaining -= c;
            }
            if (result > (__int128)CAP) return CAP + 1;
            return (long long)result;
        };

        long long total = countPerms(half, halfLen);
        long long kk = (long long)k;
        if (kk > total) return ""; // eto palindrome exist e kore na

        string halfStr;
        halfStr.reserve(halfLen);
        long long remainingLen = halfLen;

        for (long long pos = 0; pos < halfLen; pos++) {
            for (int c = 0; c < 26; c++) {
                if (half[c] == 0) continue;
                half[c]--;
                long long perms = countPerms(half, remainingLen - 1);
                if (kk <= perms) {
                    halfStr.push_back('a' + c);
                    remainingLen--;
                    break;
                } else {
                    kk -= perms;
                    half[c]++;
                }
            }
        }

        string result = halfStr;
        if (oddChar != -1) result.push_back('a' + oddChar);
        string reversedHalf = halfStr;
        reverse(reversedHalf.begin(), reversedHalf.end());
        result += reversedHalf;

        return result;
    }
};