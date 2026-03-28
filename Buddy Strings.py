class Solution(object):
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        # mismatch index collect
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
        # exactly 2 mismatch হলে swap check
        if len(diff) == 2:
            i, j = diff
            return s[i] == goal[j] and s[j] == goal[i]
        return False