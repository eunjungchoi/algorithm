# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false
# Example 4:
#
# Input: s = "([)]"
# Output: false
# Example 5:
#
# Input: s = "{[]}"
# Output: true
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack: List = []

        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            elif i in [')', '}', ']']:
                if not len(stack): return False
                top: str = stack.pop()

                if i == ')' and top != '(':
                    return False
                if i == '}' and top != '{':
                    return False
                if i == ']' and top != '[':
                    return False

        if len(stack):
            return False
        else:
            return True


# 91 / 91 test cases passed.
# Status: Accepted
# Runtime: 20 ms
# Memory Usage: 13.9 MB
#
# Your runtime beats 98.98 % of python3 submissions.
# Your memory usage beats 35.38 % of python3 submissions.
