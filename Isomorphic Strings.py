class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        map_s_t = {}
        map_t_s = {}
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            # check s -> t mapping
            if char_s in map_s_t:
                if map_s_t[char_s] != char_t:
                    return False
            else:
                map_s_t[char_s] = char_t
            # check t -> s mapping
            if char_t in map_t_s:
                if map_t_s[char_t] != char_s:
                    return False
            else:
                map_t_s[char_t] = char_s
        return True