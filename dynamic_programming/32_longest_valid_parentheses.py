# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # dynamic programming with stack
        if not s:
            return 0

        dp = [0] * (len(s) + 1)
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # 여는 괄호일 때는 무조건 stack에 해당 인덱스를 추가
            else:  # 닫는 괄호일 때는
                if stack:  # stack에  열린 괄호가 있으면
                    left = stack.pop()  # top을 빼내면 이게 여는 괄호가 됨 = left
                    dp[i + 1] = i - left + 1 + dp[left]
                    # i - left + 1 은 현재 i가 속한 valid parentheses의 length.
                    # dp[left]은 left 바로 앞 인덱스 역시 valid parentheses 일 경우 그 length를 더해줌.
                    # 연속된 longest valid parentheses를 구하는 것이기 때문에.

        return max(dp)


# 230 / 230 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Memory Usage: 14 MB
#
# Your runtime beats 97.06 % of python3 submissions.
# Your memory usage beats 67.83 % of python3 submissions.
