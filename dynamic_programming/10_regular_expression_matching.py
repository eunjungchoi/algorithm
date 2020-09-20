# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
# Example 1:
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
#
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
# Example 5:
#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false


class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:

        # dynamic programming : tabulation (bottom up)
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        # dp(i, j) : does text[i:] and pattern[j:] match
        # 둘다 뒤에서부터 체크하면서 앞으로 이동.
        dp[-1][-1] = True

        for i in range(len(text), -1, -1):    # text의 마지막 인덱스+1 부터 0까지,  1씩 감소하면서 순회.
            for j in range(len(pattern) - 1, -1, -1):   # pattern의 마지막 인덱스부터 0까지, 1씩 감소하면서 순회

                first_match = i < len(text) and pattern[j] in {text[i], '.'}

                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]

        # "aab"
        # "c*a*b"

        #    c  *  a  *  b
        # a [1, 0, 1, 0, 0, 0],  i=0
        # a [1, 0, 1, 0, 0, 0],  i=1
        # b [1, 0, 1, 0, 1, 0],  i=2
        #   [0, 0, 0, 0, 0, 1],  # dp[-1][-1] = 1로 시작.

        # [[True, False, True, False, False, False],
        #  [True, False, True, False, False, False],
        #  [True, False, True, False, True, False],
        #  [False, False, False, False, False, True]]


# 447 / 447 test cases passed.
# Status: Accepted
# Runtime: 56 ms
# Memory Usage: 13.8 MB
#
# Your runtime beats 64.35 % of python3 submissions.
# Your memory usage beats 82.46 % of python3 submissions.
