class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        # Factor contribution of each digit 0-9
        DIGIT_FACTORS = {
            0: {}, 1: {},
            2: {2: 1}, 3: {3: 1}, 4: {2: 2},
            5: {5: 1}, 6: {2: 1, 3: 1}, 7: {7: 1},
            8: {2: 3}, 9: {3: 2}
        }

        def get_prime_count(x):
            cnt = {2: 0, 3: 0, 5: 0, 7: 0}
            for p in (2, 3, 5, 7):
                while x % p == 0:
                    x //= p
                    cnt[p] += 1
            return cnt, x == 1

        def get_factor_count(need):
            """Convert required prime exponents into the fewest digits 2-9."""
            a, b, c, d = need[2], need[3], need[5], need[7]
            n8, a = divmod(a, 3)
            n9, b = divmod(b, 2)
            n4, a = divmod(a, 2)
            n2 = a
            n6 = 0
            # Prefer 6 over 2+3
            if n2 and b:
                n2 -= 1
                b -= 1
                n6 += 1
            # Prefer 6+2 over 4+3
            if b and n4:
                n4 -= 1
                b -= 1
                n2 += 1
                n6 += 1
            return {2: n2, 3: b, 4: n4, 5: c, 6: n6, 7: d, 8: n8, 9: n9}

        def construct(factors):
            return ''.join(str(d) * factors[d] for d in range(2, 10))

        def sum_values(f):
            return sum(f.values())

        need, ok = get_prime_count(t)
        if not ok:
            return "-1"

        factors = get_factor_count(need)
        if sum_values(factors) > len(num):
            return construct(factors)

        # Prefix factor counts of the whole string
        prefix = {2: 0, 3: 0, 5: 0, 7: 0}
        for ch in num:
            for p, f in DIGIT_FACTORS[int(ch)].items():
                prefix[p] += f

        first_zero = num.find('0')
        if first_zero == -1:
            first_zero = len(num)
            # num itself already works
            if all(prefix[p] >= need[p] for p in need):
                return num

        # Try to change the shortest possible suffix
        for i in range(len(num) - 1, -1, -1):
            d = int(num[i])
            # Remove contribution of the digit we are about to replace
            for p, f in DIGIT_FACTORS[d].items():
                prefix[p] -= f

            if i > first_zero:          # cannot keep a zero in the kept prefix
                continue

            space = len(num) - 1 - i    # free positions after position i
            for nd in range(d + 1, 10):
                # Remaining need after keeping the prefix and placing nd
                rem = {p: max(0, need[p] - prefix[p] - DIGIT_FACTORS[nd].get(p, 0))
                       for p in (2, 3, 5, 7)}
                fac = get_factor_count(rem)
                if sum_values(fac) <= space:
                    ones = space - sum_values(fac)
                    return (num[:i] + str(nd)
                            + '1' * ones
                            + construct(fac))

        # Need one extra digit
        fac = get_factor_count(need)
        return '1' * (len(num) + 1 - sum_values(fac)) + construct(fac)