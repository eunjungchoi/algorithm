# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
#
# Input: "cbbd"
# Output: "bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2: return s
        if s == s[::-1]: return s

        def expand_when_match(left, right):
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1

            return s[left + 1:right - 1]

        result = ""
        for i in range(len(s) - 1):
            result = max(result,
                         expand_when_match(i, i + 1),
                         expand_when_match(i, i + 2),
                         key=len)

        return result

        # last_index: int = len(s) - 1
        #
        # substring: str = s[0]
        # for i, item in enumerate(s):
        #     if len(substring) > ((last_index) - i) * 2 + 1:
        #         break
        #
        #     sub: str = item
        #     if i + 1 > last_index:
        #         break
        #
        #     key1: int = i - 1
        #     key2: int = i + 1
        #     while key1 >= 0 and s[key1] == s[key2]:
        #         sub = s[key1] + sub + s[key2]
        #         key1 -= 1
        #         key2 += 1
        #         if key1 < 0 or key2 > last_index:
        #             break
        #     if len(sub) > len(substring):
        #         substring = sub
        #
        #     sub = ""
        #     key1 = i
        #     key2 = i + 1
        #     while key1 >= 0 and s[key1] == s[key2]:
        #         sub = s[key1] + sub + s[key2]
        #         key1 -= 1
        #         key2 += 1
        #         if key1 < 0 or key2 > last_index:
        #             break
        #     if len(sub) > len(substring):
        #         substring = sub
        #
        # return substring


# after fix:
# 103 / 103 test cases passed.
# Status: Accepted
# Runtime: 268 ms
# Memory Usage: 13.7 MB
#
# Your runtime beats 93.26 % of python3 submissions.
# Your memory usage beats 92.01 % of python3 submissions.



