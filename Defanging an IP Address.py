class Solution(object):
    def defangIPaddr(self, address):
        result = []
        for ch in address:
            if ch == ".":
                result.append("[.]")
            else:
                result.append(ch)
        return "".join(result)