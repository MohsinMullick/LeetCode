"""Longest Common Prefix
Easy
Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty
"""
class Solution(object):#create a class named Solution and default value object
    def longestCommonPrefix(self, strs):  # create a method
        if not strs:  # if list is empty
            return ""
        prefix = strs[0]  # start index assume
        # print(f"Check the first index: {prefix}")#chek the first index
        for i in strs[1:]:  # now check the next all index
            # print(f"Check the next index value: {i}")#show the all  index without first index
            # Shorten the prefix until it matches the start of i
            while i[:len(prefix)] != prefix:  # check the first prefix compare second prefix value
                prefix = prefix[:-1]  # reverse value
                # print(f"Prefix shortened to: {prefix}")#jsut check value reverse
                if not prefix:  # if the value is empty like first prefix length 5 next prefix length 3
                    return ""  # No common prefix
        return prefix  # jut check values
solve = Solution()  # instance
results = solve.longestCommonPrefix(["dog","racecar","car"])  # call the method
print(results)  # print the value









