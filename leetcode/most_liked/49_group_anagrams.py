# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
#
# Input: strs = [""]
# Output: [[""]]
# Example 3:
#
# Input: strs = ["a"]
# Output: [["a"]]
#
#
# Constraints:
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lower-case English letters.

import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)

        for item in strs:
            result[''.join(sorted(item))].append(item)

        return result.values()


# 47 / 47 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Memory Usage: 13.8 MB
#
# Your runtime beats 96.32 % of python3 submissions.
# Your memory usage beats 78.92 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고. 

