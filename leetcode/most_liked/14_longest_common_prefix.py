# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.
from typing import List


class Solution:
    @staticmethod
    def longest_common_prefix(self, strs: List[str]) -> str:
        length = len(strs)
        if not length:
            return ""

        min_length = len(strs[0])
        min_item = strs[0]

        for item in strs:
            if len(item) < min_length:
                min_length = len(item)
                min_item = item

        if not min_length:
            return ""

        prefix = min_item
        for i in range(0, length):
            if not len(prefix) or not len(strs[i]):
                return ""

            key = 0
            while key < min_length and strs[i][key] == prefix[key]:
                key += 1
                if key > (len(prefix) - 1) or key > (len(strs[i]) - 1):
                    break
            prefix = prefix[:key] if key > 0 else ""

        return prefix
