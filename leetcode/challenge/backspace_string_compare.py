# Given two strings S and T, return if they are equal when both are typed into empty text editors.
#   '#' means a backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.
#
# Example 1:
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:
#
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:
#
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:
#
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# Follow up:
#
# Can you solve it in O(N) time and O(1) space?

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        if not len(S) or not len(T): return False

        new_s: str = ""
        new_t: str = ""

        for char in S:
            if char == '#':
                if len(new_s):
                    new_s = new_s[:-1]
            else:
                new_s += char

        for char in T:
            if char == '#':
                if len(new_t):
                    new_t = new_t[:-1]
            else:
                new_t += char

        return new_s == new_t


# 110 / 110 test cases passed.
# Status: Accepted
# Runtime: 24 ms
# Memory Usage: 13.8 MB

# Your runtime beats 95.77 % of python3 submissions.
# Your memory usage beats 72.46 % of python3 submissions.
