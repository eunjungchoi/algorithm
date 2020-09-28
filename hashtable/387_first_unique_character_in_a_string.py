# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode"
# return 2.
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # counter 로 글자별 설정
        # s 처음부터 순회하며 counter[key] == 1인지 체크.

        counter = collections.Counter(s)

        for i, char in enumerate(s):
            if counter[char] == 1:
                return i

        return -1


# 104 / 104 test cases passed.
# Status: Accepted
# Runtime: 84 ms
# Memory Usage: 14.3 MB
#
# Your runtime beats 93.60 % of python3 submissions.
