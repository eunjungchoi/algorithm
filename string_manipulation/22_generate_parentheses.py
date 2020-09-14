# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution:
    def generateParenthesis(self, N):
        # backtracking 으로 풀이
        results = []

        def backtrack(s='', left=0, right=0):
            if len(s) == N * 2:  # string이 N쌍 개가 되면 string이 완성된 것이므로 결과에 추가
                results.append(s)
                return
            if left < N:
                backtrack(s + '(', left + 1, right)
            if left > right:
                backtrack(s + ')', left, right + 1)

        backtrack()
        return results


# 8 / 8 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Memory Usage: 14.1 MB
#
# Your runtime beats 63.17 % of python3 submissions.
# Your memory usage beats 56.10 % of python3 submissions.
