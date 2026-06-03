class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        import sys
        from bisect import bisect_left

        def min_first_then_second(starts1, durs1, starts2, durs2):
            if not starts1 or not starts2:
                return sys.maxsize
            # Sort second rides by start time: (start, dur, end)
            second = sorted([(s, d, s + d) for s, d in zip(starts2, durs2)])
            n = len(second)
            if n == 0:
                return sys.maxsize

            # Suffix min end time
            suffix_min_end = [0] * n
            suffix_min_end[n - 1] = second[n - 1][2]
            for i in range(n - 2, -1, -1):
                suffix_min_end[i] = min(suffix_min_end[i + 1], second[i][2])

            # Prefix min duration
            prefix_min_dur = [0] * n
            prefix_min_dur[0] = second[0][1]
            for i in range(1, n):
                prefix_min_dur[i] = min(prefix_min_dur[i - 1], second[i][1])

            min_finish = sys.maxsize
            # Pre-extract starts for binary search
            second_starts = [s[0] for s in second]

            for s1, d1 in zip(starts1, durs1):
                T = s1 + d1  # end time of first ride

                # Find first ride in second with start >= T
                idx = bisect_left(second_starts, T)

                # Option 1: use a second ride starting after T (min end time)
                opt1 = suffix_min_end[idx] if idx < n else sys.maxsize

                # Option 2: use a second ride starting before T (T + min dur in prefix)
                opt2 = sys.maxsize
                if idx > 0:
                    opt2 = T + prefix_min_dur[idx - 1]

                best = min(opt1, opt2)
                min_finish = min(min_finish, best)

            return min_finish

        # Case 1: land then water
        ans1 = min_first_then_second(landStartTime, landDuration, waterStartTime, waterDuration)

        # Case 2: water then land
        ans2 = min_first_then_second(waterStartTime, waterDuration, landStartTime, landDuration)

        ans = min(ans1, ans2)
        return ans if ans != sys.maxsize else -1  # or appropriate default